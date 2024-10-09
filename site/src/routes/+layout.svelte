<script lang="ts">
    // Global styles
    import "$lib/style/global.scss";

    import ikeaIcon from "$lib/assets/ikea.svg";
    import chalmersIcon from "$lib/assets/chalmers.svg";
</script>

<nav>
    <a href="https://ikea.com/">
        <img src={ikeaIcon} alt="IKEA company logotype" />
    </a>
</nav>

<slot />

<footer>
    <img src={chalmersIcon} alt="Chalmers University of Technology logotype" />
    <h2>TEK830 Digitalization and AI in practice</h2>
</footer>

<style lang="scss">
    nav {
        padding: 0.8em;
    }

    nav a {
        margin-right: 10px;
    }

    footer {
        background-color: var(--color-bg-darker);
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 4rem;
        gap: 4rem;

        img {
            width: 6rem;
        }
    }
</style>
