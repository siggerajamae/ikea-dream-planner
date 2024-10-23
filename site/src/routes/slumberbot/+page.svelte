<script>
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

        
        const historyParam = encodeURIComponent(JSON.stringify(chatHistory)); // Convert array to JSON string and encode

        try {
            const response = await fetch(`/slumberbot?history=${encodeURIComponent(historyParam)}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const reader = response.body.getReader();
            const decoder = new TextDecoder('utf-8');
            
            let old_chatHistory = chatHistory;
            let buffer = "";
            // Read the streamed response
            while (true) {
                const { done, value } = await reader.read();
                if (done) break;

                const whole_chunk = decoder.decode(value);
                buffer += whole_chunk;
                let split_chunk = buffer.split("data: ");
                split_chunk.shift();
                let assistantResponse = "";
                try {
                    split_chunk.forEach((chunk) => {
                        // Don't crash when it sends [DONE]
                        if (chunk.includes("[DONE]")) return;
                        let cut_chunk = chunk.split("\n")[0].replace("data: ", "");

                        let chunk_data = JSON.parse(cut_chunk);
                        let content = chunk_data.choices[0].delta.content;
                        if (content == null) return;
                        assistantResponse += content;
                    });
                } catch (error) {
                    // Sometimes we get incomplete responses
                    // By saving the incomplete ones in a buffer, it will
                    // be corrected when we get the next chunk
                }
                

                chatHistory = [
                    ...old_chatHistory,
                    { role: "assistant", content: assistantResponse },
                ];
            }

        } catch (error) {
            console.error('Error:', error); // Log any errors
        }
        finally {
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
        height: 65vh;
        max-width: 800px;
        margin: 0 auto;
        font-family: "Arial", sans-serif;
        margin-bottom: 70px;
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
