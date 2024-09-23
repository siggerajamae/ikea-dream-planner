<script lang="ts">
    // Global styles
    import "$lib/style/global.scss"

    import ikeaIcon from "$lib/assets/ikea.svg";
</script>

<!-- Navigation -->
<nav>
    <a href="https://ikea.com/">
        <img src={ikeaIcon} alt="IKEA company logotype" />
    </a>
</nav>

<slot />

<footer>
    <h2>TODO</h2>
</footer>

<style lang="scss">
    nav {
        padding: .8em;
    }

    footer {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 4rem;
    }
</style>
