export type Question = {
    id: string;
    ask: string;
    method: string;
    onAnswer: (answer: any, user: Map<String, any>) => void;
    constraints?: any;
    substitutes?: string[];
    followUps?: string[];
}
