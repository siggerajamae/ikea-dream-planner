export class Question {
    ask: string;
    method: string;
    key: string;
    constraints: any;

    constructor(ask: string, key: string, field: string, constraints: any) {
        this.ask = ask;
        this.method = key;
        this.key = field
        this.constraints = constraints
    }
}
