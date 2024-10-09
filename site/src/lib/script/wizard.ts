import type { Question } from "./question"

export enum WizardState {
    GREET,
    QUESTION,
    RECOMMEND,
    END,
}

export type WizardStateData =
    | [WizardState.GREET, undefined]
    | [WizardState.QUESTION, QuestionStateData]
    | [WizardState.RECOMMEND, RecommendStateData]
    | [WizardState.END, undefined]

export class QuestionStateData {
    question: Question

    constructor(question: Question) {
        this.question = question
    }
}

export class RecommendStateData {

}

export class Wizard {
    state: WizardStateData;
    
    // Normal questions will be asked in the order that they appear in the json
    // file.
    // Conditional questions are only asked when referenced, either as
    // follow-up questions or substitute questions.
    normal: Question[];
    conditional: Question[];

    // Maintain a map of answered questions
    answers: Map<string, any>

    // Refers to the next normal question
    nextQuestionIdx: number;

    constructor(normal: Question[], conditional: Question[]) {
        this.state = [WizardState.GREET, undefined]
        this.normal = normal;
        this.conditional = conditional;
        this.nextQuestionIdx = 0
        this.answers = new Map<string, any>()
    }

    nextQuestion() {
        // Create question state data
        const question = this.normal[this.nextQuestionIdx];
        const stateData = new QuestionStateData(question)

        // Update the state
        this.state = [WizardState.QUESTION, stateData];

        // Increment the next question index
        this.nextQuestionIdx++;
    }
} 
