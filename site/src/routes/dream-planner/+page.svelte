<script lang="ts">
    import { error } from "@sveltejs/kit";
    import NumberQuestion from "./NumberQuestion.svelte";
    import type { Question } from "$lib/script/wizard/question";
    import { Recommender } from "$lib/script/wizard/recommender";
    import { fetchProductInfo } from "$lib/script/ikea/product";

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

    let wizardState: WizardState = WizardState.GREET;
</script>

<main>
    {#if wizardState == WizardState.GREET}
        <h1>Welcome to Dream Planner!</h1>
        <button
            on:click={() => {
                nextQuestion();
            }}>Begin</button
        >
    {:else if wizardState == WizardState.QUESTION}
        <h1>{currentQuestion.ask}</h1>
        {#if currentQuestion.method == "number"}
            <NumberQuestion
                min={currentQuestion.constraints.min}
                max={currentQuestion.constraints.max}
                onAnswer={(value) => {
                    user.set(currentQuestion.key, value);
                    recommend();
                }}
            />
        {/if}
    {:else if wizardState == WizardState.RECOMMEND}
        <h1>Recommendations</h1>
        <section id="products">
            {#each recommendations as product}
                <!-- svelte-ignore empty-block -->
                {#await product then product}
                    <section class="product">
                        <h2>{product.name}</h2>
                        <img src={product.mainImageUrl} alt={product.name}>
                        <p>{product.salesPrice.numeral} {product.salesPrice.currencyCode}</p>
                    </section>
                {/await}
            {/each}
        </section>
        <button on:click={nextQuestion}>Next</button>
    {:else if wizardState == WizardState.END}
        <h1>No more questions</h1>
    {/if}
</main>

<style lang="scss">
    main {
        min-height: 100vh;
        padding: 4rem;
        display: flex;
        gap: 2rem;
        flex-direction: column;
        align-items: center;
    }

    #products {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        gap: 2rem;
    }

    .product {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start; 

        img {
            width: 20rem;
        }

        p {
            font-size: 1.2rem;
        }
    }
</style>
