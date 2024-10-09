<script lang="ts">
    export let min: number;
    export let max: number;
    export let answer: number;
</script>

<input type="number" bind:value={answer} {min} {max} />
