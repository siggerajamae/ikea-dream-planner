<script lang="ts">
    import { type Question, QuestionMethod } from "$lib/script/question";
    import { Wizard, WizardState } from "$lib/script/wizard";
    import NumberMethod from "./NumberMethod.svelte";

    export let data: {
        questions: { normal: Question[]; conditional: Question[] };
    };

    let normal = data.questions.normal;
    let conditional = data.questions.conditional;

    // Create a new wizard with the questions
    let wizard = new Wizard(normal, conditional);

    // Product recommender
    let productRecommender = undefined;

    // User information TODO
    let userInfo = undefined;
</script>

<main>
    <!-- Conditional rendering, Wizard in its greeting state. Doesn't really
    make sense for actual Wizard to have a greeting state, but yaya -->
    {#if wizard.state[0] == WizardState.GREET}
        <p>Greet</p>
        <button
            on:click={() => {
                wizard.nextQuestion();

                // Trigger reacitivity
                wizard = wizard;
            }}>Begin</button
        >
        <!-- User is being asked a question -->
    {:else if wizard.state[0] == WizardState.QUESTION}
        <p>Question: {wizard.state[1].question.ask}</p>

        <!-- Render whatever needs to be onscreen for the user to
        answer the current question -->
        {#if wizard.state[1].question.method == QuestionMethod.NUMBER}
            <NumberMethod />
        {:else if wizard.state[1].question.method == QuestionMethod.LOCATION}
            <p>Location method</p>
        {:else if wizard.state[1].question.method == QuestionMethod.BINARY}
            <p>Binary method</p>
        {/if}

        <!-- If the Wizard is recommending products, render that shit -->
    {:else if wizard.state[0] == WizardState.RECOMMEND}
        <p>Recommend</p>

        <!-- The Wizard has ended -->
    {:else if wizard.state[0] == WizardState.END}
        <p>End</p>
    {/if}
</main>
