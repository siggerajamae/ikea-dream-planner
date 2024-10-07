<script lang="ts">
  import { onMount } from "svelte";
  import QuestionCard from "./QuestionCard.svelte";
  import nightlightIcon from "$lib/assets/nightlight.svg";

  interface Conditions {
    firmness: string;
    springs: string;
  }

  interface Bed {
    name: string;
    conditions: Conditions;
    image: string;
    price: Int16Array;
    score?: number; // optional
  }

  let beds: Bed[] = []; // From JSON

  // Trivial sample questions as of writing
  let questions = [
    {
      question: "What is your preferred firmness?",
      choices: ["Medium firm", "Firm"],
      key: "firmness" as keyof Conditions,
    },
    {
      question: "What type of springs do you prefer?",
      choices: ["Springs", "Pocket springs"],
      key: "springs" as keyof Conditions,
    },
  ];

  $: currentQuestionIndex = 0;
  let filteredBeds: Bed[] = []; // Holds the top beds

  let userAnswers: Partial<Record<keyof Conditions, string>> = {}; // e.g firmness: firm

  // Load bed data from JSON
  onMount(async () => {
    const response = await fetch("/products-JSON/sample-beds.json");
    beds = await response.json();
    updateRecommendations();
  });

  // Handle user selection for a question and move to the next
  function handleSelect(choice: string, questionKey: keyof Conditions) {
    userAnswers[questionKey] = choice;
    currentQuestionIndex++;
    if (currentQuestionIndex >= questions.length) {
      currentQuestionIndex = 0;
    }
    updateRecommendations();
  }

  function updateRecommendations() {
    filteredBeds = beds
      .map((bed) => {
        // Calculate match score
        let score = 0;
        for (const key in userAnswers) {
          if (
            userAnswers[key as keyof Conditions] ===
            bed.conditions[key as keyof Conditions]
          ) {
            score++;
          }
        }
        return { ...bed, score };
      })
      .sort((a, b) => b.score! - a.score!) // sort by score
      .slice(0, 4); // Show top 4
  }
</script>

<!-- Main Layout with Two Sections -->
<div class="layout">
  <!-- Left side -->
  <div class="questions">
    <QuestionCard
      question={questions[currentQuestionIndex].question}
      choices={questions[currentQuestionIndex].choices}
      icon={nightlightIcon}
      on:select={(event) =>
        handleSelect(event.detail, questions[currentQuestionIndex].key)}
    />
  </div>

  <!-- Right side -->
  <div class="beds">
    <h2>Recommended Beds</h2>
    {#each filteredBeds as bed}
      <div class="bed-card">
        <img src={bed.image} alt={bed.name} class="bed-image" />
        <div class="bed-info">
          <h3>{bed.name}</h3>
          <p>Price: {bed.price} SEK</p>
          <p>Firmness: {bed.conditions.firmness}</p>
          <p>Springs: {bed.conditions.springs}</p>
        </div>
      </div>
    {/each}
  </div>
</div>

<main>
  <!-- <h1>Dream Planner</h1>
  <section
  <div id="questions">
    <QuestionCard
      question="What is your favorite color?"
      choices={["Red", "Blue", "Green", "Yellow"]}
      icon={nightlightIcon}
    />
  </div>
  <p>Step through the questions to get personal recommendations!</p> -->
</main>

<style lang="scss">
  .layout {
    color: var(--color-text-main);
    padding: 1rem;
    gap: 2rem;
    display: flex;
    justify-content: space-between;
  }

  .questions,
  .beds {
    flex: 1;
  }

  .questions {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .beds {
    padding-left: 1rem;
    border-left: 1px solid #ddd;
  }

  .bed-card {
    display: flex;
    flex-direction: row;
    border: 1px solid #ddd;
    border-radius: 0.5rem;
    padding: 1rem;
    margin-bottom: 1rem;
    gap: 1rem;
    align-items: center;
  }

  .bed-image {
    object-fit: cover;
    border-radius: 0.5rem;
    width: 100px;
    height: 100px;
  }

  .bed-info {
    display: flex;
    flex-direction: column;
  }

  .bed-info h3 {
    margin: 0;
    font-size: 1.2rem;
  }

  .bed-info p {
    margin: 0.2rem 0;
    font-size: 1rem;
  }
</style>
