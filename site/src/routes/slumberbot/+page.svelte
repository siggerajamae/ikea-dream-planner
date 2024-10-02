<script>
    import OpenAI from "openai";

    let textInput = ""; // This will hold the value of the textbox
    let chatHistory = [];
    let waitingForResponse = false;

    async function handleSubmit() {
        if (!textInput.trim()) {
            return;
        }
        // Don't let the user start a question without the last one finishing
        if (waitingForResponse) return;
        waitingForResponse = true;

        // Add input to chat history
        chatHistory = [...chatHistory, { role: "user", content: textInput }];
        textInput = ""; // Clear the input after adding it to chat history

        // Set up OpenAI API client
        const openai = new OpenAI({
            dangerouslyAllowBrowser: true,
            apiKey: import.meta.env.VITE_OPENAI_API_KEY,
        });

        try {
            const res = await fetch(
                "https://api.openai.com/v1/chat/completions",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        Authorization: `Bearer ${openai.apiKey}`,
                    },
                    body: JSON.stringify({
                        model: "gpt-4",
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

            const reader = res.body.getReader();
            const decoder = new TextDecoder("utf-8");
            let assistantResponse = "";

            let old_chatHistory = chatHistory;
            // Read the responses in a stream
            // Otherwise, we have to wait ~5-10 seconds for the whole response at once
            while (true) {
                const { done, value } = await reader.read();
                if (done) break;

                const whole_chunk = decoder.decode(value);
                let split_chunk = whole_chunk.split("data: ");
                split_chunk.shift();
                split_chunk.forEach((chunk) => {
                    // Don't crash when it sends [DONE]
                    if (chunk.includes("[DONE]")) return;
                    let cut_chunk = chunk.split("\n")[0].replace("data: ", "");

                    let chunk_data = JSON.parse(cut_chunk);
                    let content = chunk_data.choices[0].delta.content;
                    if (content == null) return;
                    assistantResponse += content;
                });

                chatHistory = [
                    ...old_chatHistory,
                    { role: "assistant", content: assistantResponse },
                ];
            }
        } catch (error) {
            console.error("Error with API call:", error);
        } finally {
            waitingForResponse = false;
        }
    }

    import { onMount } from "svelte";

    onMount(() => {
        document.addEventListener("keydown", function (event) {
            if (event.key === "Enter") {
                handleSubmit();
            }
        });
        setTimeout(() => {
            chatHistory = [
                {
                    role: "assistant",
                    content:
                        "Hello! How can I assist you today? Are you having trouble sleeping?",
                },
            ];
        }, 500);
    });
</script>

<!-- HTML structure -->
<div id="chat-wrapper">
    <div id="chat-container">
        {#each chatHistory as message}
            <div
                class={message.role === "user"
                    ? "user-message"
                    : "assistant-message"}
            >
                <p>
                    <strong
                        >{message.role === "user"
                            ? "You: "
                            : "Slumberbot: "}</strong
                    >{message.content}
                </p>
            </div>
        {/each}
    </div>
    <div id="input-container">
        <input
            type="text"
            bind:value={textInput}
            placeholder="Enter your message..."
        />
        <button on:click={handleSubmit}>Submit</button>
    </div>
</div>

<style>
    #chat-wrapper {
        display: flex;
        flex-direction: column;
        height: 500px;
        max-width: 800px;
        margin: 0 auto;
        font-family: "Arial", sans-serif;
    }

    #chat-container {
        flex-grow: 1;
        overflow-y: auto;
        padding: 20px;
        background-color: #292929;
        border-radius: 10px;
        display: flex;
        flex-direction: column;
    }

    .user-message,
    .assistant-message {
        max-width: 75%;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 8px 0;
        font-size: 0.95rem;
        line-height: 1.4;
        background-color: #424242;
        color: white;
        white-space: pre-line;
    }

    .user-message {
        align-self: flex-end;
        text-align: right;
    }

    .assistant-message {
        align-self: flex-start;
        text-align: left;
    }

    #input-container {
        display: flex;
        padding: 10px;
        background-color: #292929;
        border-radius: 10px;
        margin-top: 10px;
    }

    input {
        background-color: #424242;
        color: white;
        flex-grow: 1;
        padding: 10px;
        border: 1px solid black;
        border-radius: 5px;
        font-size: 1rem;
        margin-right: 10px;
    }

    button {
        padding: 10px 20px;
        background-color: #424242;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1rem;
    }

    button:hover {
        background-color: #0056b3;
    }
</style>
