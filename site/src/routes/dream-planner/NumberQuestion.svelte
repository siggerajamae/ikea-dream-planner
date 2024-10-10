<script lang="ts">
    export let min: number;
    export let max: number;
    export let onAnswer: (value: number) => void;
    let value: number = min;
</script>

<input type="number" bind:value {min} {max} />

<button on:click={() => onAnswer(value)}>Answer</button>
