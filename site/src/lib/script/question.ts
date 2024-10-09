export enum QuestionMethod {
    CHOICE = "CHOICE",
    NUMBER = "NUMBER",
    LOCATION = "LOCATION"
}

export class ChoiceQuestionMethodData {
    choices: string[];

    constructor(choices: string[]) {
        this.choices = choices
    }
}

export class NumberQuestionMethodData {
    min: number;
    max: number;

    constructor(min: number, max: number) {
        this.min = min
        this.max = max
    }
}

export class LocationQuestionMethodData {
    // TODO
}

export type QuestionMethodData =
    [QuestionMethod.NUMBER, NumberQuestionMethodData] |
    [QuestionMethod.CHOICE, ChoiceQuestionMethodData] |
    [QuestionMethod.LOCATION, LocationQuestionMethodData]


export class Question {
    // Unique identifier
    id: String;

    // What is being asked
    ask: String;

    // The method that will be used to answer the question
    methodData: QuestionMethodData;

    // Questions that should be pushed onto the question stack if the question
    // was answered or skipped, respectively
    followUpQuestions: undefined | number[];
    substituteQuestions: undefined | number[];

    constructor(
        id: String,
        ask: String,
        methodData: QuestionMethodData,
        followUpQuestions: undefined | number[] = undefined, // Optional
        substituteQuestions: undefined | number[] = undefined // Optional
    ) {
        this.id = id;
        this.ask = ask;
        this.methodData = methodData;
        this.followUpQuestions = followUpQuestions;
        this.substituteQuestions = substituteQuestions;
    }

    answer() {
        // TODO
    }
}
