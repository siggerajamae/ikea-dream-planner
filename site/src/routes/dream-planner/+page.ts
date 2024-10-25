import { type Question } from "$lib/script/wizard/question"

export async function load() {
    const normal: Question[] = [
        {
            id: "TIME_WAKE",
            ask: "At what time do you usually wake up in the morning?",
            method: "time",
            onAnswer: (answer, user) => {
                user.set("timeWake", answer)
            },
            followUps: ["TIME_SUNRISE"]
        },
        {
            id: "NOISE",
            ask: "Do you experience a lot of noise where you live?",
            method: "choice",
            constraints: {
                choices: ["yes", "no"]
            },
            onAnswer: (answer, user) => {
                user.set("noise", answer)
            },
        },
        {
            id: "AIR",
            ask: "How is the air quality where you live?",
            method: "choice",
            constraints: {
                choices: ["poor", "good"]
            },
            onAnswer: (answer, user) => {
                user.set("airQuality", answer)
            },
        },
        {
            id: "TEMP",
            ask: "What is the temperature in your room at night? (C°)",
            method: "number",
            constraints: {
                min: 0,
                max: 50
            },
            onAnswer: (answer, user) => {
                user.set("temperature", answer)
            },
        },
        {
            id: "MATTRESS_TYPE",
            ask: "What kind of mattress type do you prefer?",
            method: "choice",
            constraints: {
                choices: ["soft", "medium", "firm"]
            },
            onAnswer: (answer, user) => {
                user.set("mattressType", answer)
            },
        },
    ]
    const conditional: Question[] = [
        {
            id: "TIME_SUNRISE",
            ask: "At what time is sunrise where you live?",
            method: "time",
            onAnswer: (answer, user) => {
                user.set("timeSunrise", answer)
                let timeWake = user.get("timeWake")
                if (timeWake != null) {
                    let lightHours = (timeWake - answer) / 60
                    user.set("lightHours", lightHours)
                }
            },
        },
    ]

    // Import product conditions
    // This should really be done on the server-side
    // Big, fat TODO
    const productConditions = await import("$lib/json/wizard/productConditions.json")

    return {
        questions: {
            normal: normal,
            conditional: conditional
        },
        productConditions: productConditions.default
    }
}
