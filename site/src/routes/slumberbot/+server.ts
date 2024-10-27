// src/routes/dream-planner/+server.ts

import type { RequestHandler } from '@sveltejs/kit';

import OpenAI from "openai";

export const POST: RequestHandler = async ({ request }) => {
    let chatHistory;

    try {
        // Parse the request body as JSON
        const requestBody = await request.json();
        
        // Validate that chat history exists in the body
        if (!requestBody.historyParam) {
            return new Response('No data provided', { status: 400 });
        }

        // Try to parse the historyParam from the request body
        chatHistory = JSON.parse(requestBody.historyParam);

    } catch (e) {
        return new Response('Invalid data format', { status: 400 });
    }

    // Set up OpenAI API client
    const openai = new OpenAI({
        apiKey: import.meta.env.VITE_OPENAI_API_KEY,
    });

    try {
        const response = await fetch(
            "https://api.openai.com/v1/chat/completions",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${openai.apiKey}`,
                },
                body: JSON.stringify({
                    model: "gpt-3.5-turbo",
                    messages: [
                        {
                            role: "system",
                            content: `You are a bot whose goal is to help
                                    people sleep. Your owner is IKEA. You should
                                    only discuss things that could help people
                                    sleep, our things about IKEA.`,
                        },
                        {
                            role: "system",
                            content: `Remember the following IKEA product names well:
                                    when you say them exactly as stated here, the user
                                    will be shown a card of the product.
                                    "MALM"
                                    "SÄBOVIK"`,
                        },
                        {
                            role: "system",
                            content: `You are not ChatGPT and are not
                                    created by OpenAI, and you shall not make any
                                    mention of that.`,
                        },
                        {
                            role: "system",
                            content: `Start the conversation by asking the user
                                    why they think they are having trouble
                                    falling asleep, and then help them from
                                    there. Do not discuss IKEA products unless
                                    the user makes a mention of them.`,
                        },
                        ...chatHistory,
                    ],
                    stream: true,
                }),
            },
        );
        // Stream OpenAI response directly to the client
        return new Response(response.body, {
            headers: {
                'Content-Type': 'text/event-stream',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive'
            }
        });
    } catch (error) {
        console.error('Error:', error); // Log any errors
        return new Response(`Oopsie daisy: ${error}`);
    }

    
};
