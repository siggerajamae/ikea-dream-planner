<script lang="ts">
    // Global styles
    import "$lib/style/global.scss";

    import ikeaIcon from "$lib/assets/ikea.svg";
    import chalmersIcon from "$lib/assets/chalmers.svg";
    import HomeIcon from "$lib/components/icons/HomeIcon.svelte";
</script>

<nav>
    <a href="https://ikea.com/">
        <img src={ikeaIcon} alt="IKEA company logotype" />
    </a>
    <a href="/">
        <div class="icon">
            <HomeIcon />
        </div>
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
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 2rem;

        .icon {
            width: 3rem;
        }
    }

    footer {
        background-color: var(--color-bg-darker);
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 4rem;
        gap: 4rem;
        text-align: center;

        img {
            width: 6rem;
        }

        h2 {
            margin: 0;
            padding: 0;
            font-size: 1.1em;
        }
    }

    @media only screen and (max-width: 600px) {
        nav {
            justify-content: space-between;
        }

        footer {
            flex-direction: column;
        }
    }
</style>
