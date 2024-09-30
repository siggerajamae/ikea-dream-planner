<script>
    import ToolCard from "./ToolCard.svelte";
    import nightlightIcon from "$lib/assets/nightlight.svg";
    import botIcon from "$lib/assets/bot.svg";
    import closetIcon from "$lib/assets/checkroom.svg";
    import gogglesIcon from "$lib/assets/goggles.svg";
</script>

<main>
    <h1>Sleep with IKEA</h1>
    <section>
        <h2>Difficulties sleeping?</h2>
        <p>
            You're not alone. Millions of adults struggle with sleep issues
            every night, with about 1 in 3 experiencing insomnia or difficulty
            falling and staying asleep. From stress and anxiety to irregular
            routines and lifestyle choices, many factors can affect your ability
            to rest. Poor sleep not only leads to fatigue but also impacts mood,
            productivity, and long-term health. Whether you're tossing and
            turning or waking up frequently during the night, finding a solution
            to improve your sleep quality is essential for your overall
            well-being. One of our many goals at IKEA is to help our customers
            with improving their sleep. Explore some of our tools below,
            designed to make you comfortable.
        </p>
    </section>
    <section>
        <h2>Explore tools</h2>
        <div id="tools">
            <ToolCard
                name={"Dream Planner"}
                description={`Get help furnishing your room for your specific
                sleeping needs.`}
                icon={nightlightIcon}
                href={"#"}
            />
            <ToolCard
                name={"Slumber Bot"}
                description={`Knows everything there is to know about sleeping,
                and how our different products affect sleep!`}
                icon={botIcon}
                href={"slumberbot"}
            />
            <ToolCard
                name={"Night Closet"}
                description={`This is not a portal to Narnia, but perhaps
                something even better?`}
                icon={closetIcon}
                href={"#"}
            />
            <ToolCard
                name={"Moon Goggles"}
                description={`Stare into the sun for too long and you go blind,
                but what about the moon?`}
                icon={gogglesIcon}
                href={"#"}
            />
        </div>
    </section>
    <section>
        <h2>Improving Sleep in Asia</h2>
        <p>TODO</p>
    </section>
</main>

<style lang="scss">
    main {
        color: var(--color-text-main);
        padding: 1rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    section {
        width: 40rem;
    }

    #tools {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: repeat(2, 1fr);
        gap: 1.1rem;
    }
</style>
