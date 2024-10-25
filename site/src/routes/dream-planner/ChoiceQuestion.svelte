<script lang="ts">
    export let choices: string[];
    export let onAnswer: (value: string) => void;
</script>

<div class="row">
    <div class="button-group">
        {#each choices as choice}
            <button
                on:click={() => {
                    onAnswer(choice);
                }}
            >
                {choice}
            </button>
        {/each}
    </div>
</div>

<style lang="scss">
    .row {
        display: flex;
        gap: 2rem;
    }

    button::first-letter {
        text-transform: capitalize;
    }
</style>
