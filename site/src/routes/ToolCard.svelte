<script lang="ts">
    export let name;
    export let description;
    export let icon;
    export let href;
</script>

<a {href} class="tool-card">
    <section>
        <div class="header-icon">
            <h3>{name}</h3>
            <img src={icon} alt={`${name} icon`} />
        </div>
        <p>{description}</p>
    </section>
</a>

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

    .tool-card {
        border: 0.15rem solid;
        border-radius: 0.6rem;
        padding: 1.2rem;

        p {
            margin: 0;
        }

        h3 {
            margin-top: 0;
            margin-bottom: 0.5em;
        }
    }
</style>
