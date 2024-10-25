<script lang="ts">
    export let min: number;
    export let max: number;
    export let onAnswer: (value: number) => void;
    let value: number = min;
</script>

<div class="row">
    <input type="number" bind:value {min} {max} />

    <div class="button-group">
        <button
            on:click={() => {
                if (value == null) {
                    return;
                }
                if (value < min) {
                    onAnswer(min);
                } else if (value > max) {
                    onAnswer(max);
                } else {
                    onAnswer(max);
                }
            }}>Answer</button
        >
    </div>
</div>

<style lang="scss">
    .row {
        display: flex;
        gap: 2rem;
    }
</style>
