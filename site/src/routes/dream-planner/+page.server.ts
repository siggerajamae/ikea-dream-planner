import { LocationQuestionMethodData, NumberQuestionMethodData, Question, QuestionMethod, type QuestionMethodData } from "$lib/script/question";

function mapPlainToQuestion(obj: any) {
    const methodName = obj.methodName as QuestionMethod;
    let method: QuestionMethodData;

    switch (methodName) {
        case QuestionMethod.NUMBER: {
            const methodData: NumberQuestionMethodData = new NumberQuestionMethodData(obj.methodData.min);
            method = [methodName, methodData]
        }
        case QuestionMethod.CHOICE: {
            const methodData: NumberQuestionMethodData = new NumberQuestionMethodData(obj.methodData.min);
            method = [methodName, methodData]
        }
        case QuestionMethod.LOCATION: {
            const methodData: LocationQuestionMethodData = obj.methodData;
            method = [methodName, methodData]
        }
    }

    return new Question(
        obj.id,
        obj.ask,
        method,
        obj.followUpQuestions,
        obj.substituteQuestions
    );
}

export async function load() {
    const json = await import("$lib/json/questions.json").then(file => file);
    const normal = json.normal.map(obj => mapPlainToQuestion(obj));
    const conditional = json.conditional.map(obj => mapPlainToQuestion(obj));
    return {
        questions: {
            normal: structuredClone(normal), conditional: structuredClone(conditional)
        }
    };
}
