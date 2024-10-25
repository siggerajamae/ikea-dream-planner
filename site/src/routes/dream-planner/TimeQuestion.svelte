<script lang="ts">
    export let onAnswer: (value: number) => void;
    let value: string;
</script>

<div class="row">
    <input type="time" bind:value />
    <div class="button-group">
        <button
            on:click={() => {
                if (value != undefined) {
                    let split = value.split(":");
                    let hour = parseInt(split[0]);
                    let minute = parseInt(split[1]);
                    onAnswer(hour * 60 + minute);
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
