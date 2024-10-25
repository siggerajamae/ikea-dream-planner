<script>
    import ToolCard from "./ToolCard.svelte";

    // Icons
    import NightlightIcon from "$lib/components/icons/NightlightIcon.svelte";
    import BotIcon from "$lib/components/icons/BotIcon.svelte";
    import CheckroomIcon from "$lib/components/icons/CheckroomIcon.svelte";
    import GogglesIcon from "$lib/components/icons/GogglesIcon.svelte";
</script>

<main>
    <div class="content">
        <h1>IKEA Comfort Zone</h1>
        <section>
            <h2>Difficulties sleeping?</h2>
            <p>
                You're not alone. Millions of adults struggle with sleep issues
                every night, with about one in three experiencing insomnia or
                difficulty falling and staying asleep. From stress and anxiety
                to irregular routines and lifestyle choices, many factors can
                affect your ability to rest. Poor sleep not only leads to
                fatigue but also impacts mood, productivity, and long-term
                health. Whether you're tossing and turning or waking up
                frequently during the night, finding a solution to improve your
                sleep quality is essential for your overall well-being. One of
                our many goals at IKEA is to help our customers with improving
                their sleep. Explore some of our tools below, designed to make
                you comfortable.
            </p>
        </section>
        <section>
            <h2>Explore tools</h2>
            <div id="tools">
                <ToolCard
                    name={"Dream Planner"}
                    description={`Get help furnishing your room for your specific
                sleeping needs.`}
                    icon={NightlightIcon}
                    href={"dream-planner"}
                />
                <ToolCard
                    name={"Slumber Bot"}
                    description={`Knows everything there is to know about sleeping,
                and how our different products affect sleep!`}
                    icon={BotIcon}
                    href={"slumberbot"}
                />
                <ToolCard
                    name={"Night Closet"}
                    description={`This is not a portal to Narnia, but perhaps
                something even better?`}
                    icon={CheckroomIcon}
                    href={"#"}
                />
                <ToolCard
                    name={"Moon Goggles"}
                    description={`Stare into the sun for too long and you go blind,
                but what about the moon?`}
                    icon={GogglesIcon}
                    href={"#"}
                />
            </div>
        </section>
        <section>
            <h2>Improving sleep in Asia</h2>
            <section>
                <h3>Design principles</h3>
                <section>
                    <h4>Usability</h4>
                    <p>
                        Our tools are designed with young East Asians in mind,
                        but can generally be utilized by anyone who seeks tips
                        or inspiration on how to improve their sleeping comfort.
                        In our research, we found that a significant portion of
                        the population in countries such as South Korea and
                        Japan struggle with sleep, where some primary factors
                        are stress, noise and air pollution and heat.
                    </p>
                    <p>
                        IKEA offers products that can help with these issues,
                        and we aim to create a space where users can easily
                        discover existing solutions tailored to their individual
                        needs. With this solution we hope to bring a more
                        interactive experience over IKEA's existing web pages
                        with general information on sleep and product
                        recommendations.
                    </p>
                </section>
                <section>
                    <h4>Feasibility</h4>
                    <p>
                        For our innovation, we have decided to work almost
                        exclusively with the web framework SvelteKit. Svelte
                        provides a straightforward developer experience for
                        creating and deploying web pages, and due to the
                        relatively simple nature of the tools themselves,
                        writing our backend in TypeScript is feasible. The
                        innovation does not require any special data beyond the
                        product information available on IKEA's own website and
                        user information provided by the users themselves. The
                        product data is collected, and each product is
                        automatically annotated with tags that can then be used
                        to train models for product recommendations. Since user
                        information may include sensitive data such as location
                        details, this data must be handled with care.
                    </p>
                </section>
                <section>
                    <h4>Viability</h4>
                    <p>
                        Our innovation aligns with IKEA's vision of improving
                        living by enhancing the shopping experience with
                        interactive tools focused on improving sleep. We believe
                        that innovation is viable, and can be implemented in
                        reasonable a time frame, without the burden of
                        maintenance, as the software easily could be designed to
                        update itself when new products are added to the
                        catalog. For this reason, the idea is essentially
                        without risk, simply improving customer experience.
                    </p>
                </section>
            </section>
            <section>
                <h3>Demonstration</h3>
                <p>
                    As of writing this, the general idea of Slumber Bot and
                    Dream Planner should be communicated through what has been
                    implemented so far. Click on the card for either of these
                    tools to navigate to their respective pages. Night Closet
                    and Moon Goggles are still just placeholders, and we are
                    exploring the idea of a catalog-sleeping-podcast.
                </p>
            </section>
        </section>
        <section id="section-team">
            <h2>Our team</h2>
            <div id="team-members">
                <section>
                    <img src="/team/andersson.jpg" alt="Joshua Andersson" />
                    <h3>Joshua Andersson</h3>
                    <a href="mailto:jeffmar@student.chalmers.se"
                        >jeffmar@student.chalmers.se</a
                    >
                </section>
                <section>
                    <img src="/team/hulthe.jpg" alt="Rasmus Hulthe" />
                    <h3>Rasmus Hulthe</h3>
                    <a href="mailto:rasmushu@student.chalmers.se"
                        >rasmushu@student.chalmers.se</a
                    >
                </section>
                <section>
                    <img src="/team/rajamae.jpg" alt="Sigge Rajamäe" />
                    <h3>Sigge Rajamäe</h3>
                    <a href="mailto:siggera@student.chalmers.se"
                        >siggera@student.chalmers.se</a
                    >
                </section>
                <section>
                    <img src="/team/soderberg.jpg" alt="Elias Söderberg" />
                    <h3>Elias Söderberg</h3>
                    <a href="elisod@student.chalmers.se"
                        >elisod@student.chalmers.se</a
                    >
                </section>
            </div>
        </section>
    </div>
</main>

<style lang="scss">
    main {
        color: var(--color-text-main);
        padding: 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .content {
        display: flex;
        flex-direction: column;
        align-items: center;
        max-width: 40rem;
    }

    section {
        margin-top: 1.2rem;
        margin-bottom: 1.2rem;
    }

    #section-team {
        h2 {
            text-align: center;
        }
    }

    #tools {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: repeat(2, 1fr);
        gap: 1.1rem;
    }

    #team-members {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: repeat(2, 1fr);
        gap: 3rem;
        padding: 2rem;

        section {
            width: auto;
            margin: 0;
            text-align: center;
            overflow: hidden;

            img {
                aspect-ratio: 1;
                width: 70%;
                object-fit: cover;
                object-position: center;
                border-radius: 50%;
            }

            h3 {
                font-size: 1.2em;
                margin-bottom: 0.3em;
            }

            a {
                font-size: 0.8em;
            }
        }
    }

    @media only screen and (max-width: 600px) {
        #team-members {
            grid-template-columns: 1fr;
            grid-template-rows: repeat(4, 1fr);
        }

        #tools {
            grid-template-columns: 1fr;
            grid-template-rows: repeat(4, 1fr);
        }
    }
</style>
