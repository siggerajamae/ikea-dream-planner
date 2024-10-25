<script lang="ts">
    import { error } from "@sveltejs/kit";
    import NumberQuestion from "./NumberQuestion.svelte";
    import type { Question } from "$lib/script/wizard/question";
    import { Recommender } from "$lib/script/wizard/recommender";
    import { fetchProductInfo } from "$lib/script/ikea/product";
    import { fade, fly } from "svelte/transition";
    import TimeQuestion from "./TimeQuestion.svelte";
    import ArrowForward from "$lib/components/icons/ArrowForward.svelte";
    import ProductCard from "./ProductCard.svelte";
    import ChoiceQuestion from "./ChoiceQuestion.svelte";

    enum WizardState {
        GREET,
        QUESTION,
        RECOMMEND,
        END,
    }

    function nextQuestion() {
        // No more questions, end the wizard
        if (questionStack.length == 0) {
            wizardState = WizardState.END;
            return;
        }

        // Update the state
        wizardState = WizardState.QUESTION;

        // Pop a question from the stack
        let popped = questionStack.pop();
        currentQuestion =
            popped != undefined
                ? popped
                : // Something went very wrong here
                  error(500, "question stack empty");
    }

    function onAnswer(answer: any) {
        currentQuestion.onAnswer(answer, user);

        // If the current question has followups: push them onto the stack
        // Else, recommend
        if (
            currentQuestion.followUps != undefined &&
            currentQuestion.followUps.length > 0
        ) {
            pushFollowups();
            nextQuestion();
        } else {
            recommend();
        }
    }

    function onSkip() {
        let substituteIds = currentQuestion.substitutes;
        if (substituteIds != undefined) {
            let substitutes = substituteIds.map((id) => {
                let question = data.questions.conditional.find((question) => {
                    return id == question.id;
                });
                if (question == undefined) {
                    throw Error(
                        `referenced substitute question ${id} on ${currentQuestion.id} does not exist`,
                    );
                }
                return question;
            });
            substitutes.reverse();
            questionStack.push(...substitutes);
        }
        recommend(); // Put in the recommend state, in case this was a folloup question
    }

    function pushFollowups() {
        // Check for follow ups!
        let followUpIds = currentQuestion.followUps;
        if (followUpIds != undefined) {
            let followUps = followUpIds.map((id) => {
                let question = data.questions.conditional.find((question) => {
                    return id == question.id;
                });
                if (question == undefined) {
                    throw Error(
                        `referenced followup question ${id} on ${currentQuestion.id} does not exist`,
                    );
                }
                return question;
            });
            followUps.reverse();
            questionStack.push(...followUps);
        }
    }

    function recommend() {
        // Check if there are any new recommendations based on the current user information
        const productIds = recommender.recommend(user);

        if (productIds.length > 0) {
            // Fetch the product data for each product
            recommendations = productIds.map(async (id) => {
                return await fetchProductInfo(id);
            });

            // Move to the recommendation state if there are new products to recommend
            wizardState = WizardState.RECOMMEND;

            // TODO: Fetch information for recommended products, and then display this information
        } else {
            // Otherwise move onto the next question
            nextQuestion();
        }
    }

    export let data;

    const recommender = new Recommender(data.productConditions);
    let recommendations: any[];

    // User information key/value
    const user: Map<string, any> = new Map();

    // The question stack is the array of normal questions, reversed
    const questionStack = data.questions.normal.reverse();
    let currentQuestion: Question;

    $: wizardState = WizardState.GREET;
</script>

<main>
    {#if wizardState == WizardState.GREET}
        <div
            class="state-container"
            in:fly={{ x: 200 }}
            out:fly|local={{ x: -200 }}
        >
            <h1>Welcome to Dream Planner!</h1>
            <button
                on:click={() => {
                    nextQuestion();
                }}>Begin</button
            >
        </div>
    {:else if wizardState == WizardState.QUESTION}
        <div
            class="state-container"
            in:fly={{ x: 200 }}
            out:fly|local={{ x: -200 }}
        >
            <div class="question-transition-container">
                {#key currentQuestion}
                    <div
                        class="question-container"
                        in:fly={{ x: 200 }}
                        out:fly|local={{ x: -200 }}
                    >
                        <div class="question-ask-row">
                            <h1>{currentQuestion.ask}</h1>
                            <button
                                class="no-border"
                                on:click={() => {
                                    onSkip();
                                }}
                            >
                                <span>Skip</span>
                                <div class="icon">
                                    <ArrowForward />
                                </div>
                            </button>
                        </div>
                        {#if currentQuestion.method == "number"}
                            <NumberQuestion
                                min={currentQuestion.constraints.min}
                                max={currentQuestion.constraints.max}
                                {onAnswer}
                            />
                        {:else if currentQuestion.method == "time"}
                            <TimeQuestion {onAnswer} />
                        {:else if currentQuestion.method == "choice"}
                            <ChoiceQuestion
                                choices={currentQuestion.constraints.choices}
                                {onAnswer}
                            />
                        {/if}
                    </div>
                {/key}
            </div>
        </div>
    {:else if wizardState == WizardState.RECOMMEND}
        <div
            class="state-container"
            in:fly={{ x: 200 }}
            out:fly|local={{ x: -200 }}
        >
            <h1>Then maybe you would like...</h1>
            <section id="products">
                {#each recommendations as product}
                    <!-- svelte-ignore empty-block -->
                    {#await product then product}
                        <div transition:fade>
                            <ProductCard {product} />
                        </div>
                    {/await}
                {/each}
            </section>
            <button on:click={nextQuestion}>Next</button>
        </div>
    {:else if wizardState == WizardState.END}
        <div
            class="state-container end-container"
            in:fly={{ x: 200 }}
            out:fly|local={{ x: -200 }}
        >
            <h1>That was all the questions we had!</h1>
            <p>
                Hope you were able to find some products to help you sleep
                better!
            </p>
            <a href="/"><button>Return home</button></a>
        </div>
    {/if}
</main>

<style lang="scss">
    main {
        min-height: 100vh;
        padding: 4rem;
        box-sizing: border-box;

        &,
        .question-transition-container {
            display: grid;
        }

        .state-container,
        .question-container {
            display: flex;
            flex-direction: column;
            gap: 2rem;
            align-items: center;
            grid-column-start: 1;
            grid-column-end: 2;
            grid-row-start: 1;
            grid-row-end: 2;
        }

        .end-container {
            h1,
            p {
                padding: 0;
                margin: 0;
            }

            p {
                font-size: 1.4rem;
            }
        }
    }

    .question-ask-row {
        &,
        > button {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        .icon {
            :global(svg) {
                width: 2rem;
                fill: var(--color-text-main);
            }
        }
    }

    #products {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        gap: 2rem;
        transition: ease-in-out .2s;
    }
</style>
