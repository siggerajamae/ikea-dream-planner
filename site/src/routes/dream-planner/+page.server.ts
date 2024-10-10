import { Question } from "$lib/script/wizard/question"

function mapToQuestion(obj: any) {
    return new Question(obj.ask, obj.key, obj.field, obj.constraints)
}

export async function load() {
    // Import qustions and map to Question
    const questions = await import("$lib/json/wizard/questions.json")
    const normal = questions.normal.map(obj => { return mapToQuestion(obj) })
    const conditional = questions.normal.map(obj => { return mapToQuestion(obj) })

    // Import product conditions
    // This should really be done on the server-side
    // Big, fat TODO
    const productConditions = await import("$lib/json/wizard/productConditions.json")

    return {
        questions: {
            normal: structuredClone(normal),
            conditional: structuredClone(conditional)
        },
        productConditions: structuredClone(productConditions.default)
    }
}
