<script lang="ts">
    import { createEventDispatcher } from "svelte";

    export let question: string;
    export let choices: string[]; // Array of choices
    export let icon;

    let selectedChoice: string = "";

    const dispatch = createEventDispatcher();

    const handleSelect = (choice: string) => {
        selectedChoice = choice;
        dispatch("select", choice);
    };
</script>

<div class="question-card">
    <section>
        <div class="header-icon">
            <h3>{question}</h3>
            <svelte:component this={icon} />
        </div>

        <div class="choices">
            {#each choices as choice}
                <button
                    class:selected={selectedChoice === choice}
                    on:click={() => handleSelect(choice)}
                >
                    {choice}
                </button>
            {/each}
        </div>
    </section>
</div>

<style lang="scss">
    .header-icon {
        display: flex;
        justify-content: space-between;
        align-items: start;
        gap: 1rem;

        img {
            height: 2rem;
        }
    }

    .question-card {
        border: 0.15rem solid;
        border-radius: 0.6rem;
        padding: 1.2rem;
        margin-bottom: 1rem;

        h3 {
            margin-top: 0;
            margin-bottom: 0.5em;
        }
    }

    .choices {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;

        button {
            border: 0.1rem solid;
            border-radius: 0.5rem;
            padding: 0.6rem;
            background-color: white;
            cursor: pointer;
            text-align: left;
        }

        button:hover {
            background-color: #f0f0f0;
        }

        button.selected {
            background-color: #d4edda;
            border-color: #28a745;
        }
    }
</style>
