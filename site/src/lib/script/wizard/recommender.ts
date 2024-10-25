export class Recommender {
    // Maintain a list of products that have been recommended
    private recommended: Set<string>
    private productConditions: any[]

    constructor(productConditions: any[]) {
        this.recommended = new Set()
        this.productConditions = productConditions
    }

    isMatch(user: Map<string, any>, condition: any): boolean {
        switch (condition.type) {
            case ("and"): {
                return this.isMatch(user, condition.left) && this.isMatch(user, condition.right)
            }
            case ("or"): {
                return this.isMatch(user, condition.left) || this.isMatch(user, condition.right)
            }
            case ("geq"): {
                const value = user.get(condition.key)

                if (value == undefined) {
                    return false
                }
                return value >= condition.value
            }
            case ("leq"): {
                const value = user.get(condition.key)
                if (value == undefined) {
                    return false
                }
                return value <= condition.value
            }
            case ("eq"): {
                const value = user.get(condition.key)
                if (value == undefined) {
                    return false
                }
                return value == condition.value
            }
            default: {
                throw Error(`unrecongnized condition type ${condition.type}`)
            }
        }
    }

    // Make recommendations based on the current user information
    recommend(user: Map<string, any>): string[] {
        const products: Set<string> = new Set()
        for (const product of this.productConditions) {
            for (const condition of product.conditions) {
                if (this.isMatch(user, condition)) {
                    products.add(product.id)
                    continue
                }
            }
        }

        // Don't make the same recommendation twice
        const fresh = products.difference(this.recommended)
        fresh.forEach((product) => { this.recommended.add(product) })

        return Array.from(fresh.values())
    }
}
