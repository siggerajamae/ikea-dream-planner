<script lang="ts">
    export let name;
    export let description;
    export let icon;
    export let href;
</script>

<a {href} class="tool-card">
    <section>
        <div class="top-row">
            <h3>{name}</h3>
            <svelte:component this={icon} class="icon" />
        </div>
        <p>{description}</p>
    </section>
</a>

<style lang="scss">
    .top-row {
        display: flex;
        justify-content: space-between;
        align-items: start;
        gap: 1rem;

        :global(svg) {
            fill: var(--color-bg-main);
        }
    }

    .tool-card {
        border-radius: 0.6rem;
        padding: 1.2rem;
        background-color: var(--color-text-main);
        color: var(--color-bg-main);

        p {
            margin: 0;
        }

        h3 {
            margin-top: 0;
            margin-bottom: 0.5em;
        }
    }
</style>
