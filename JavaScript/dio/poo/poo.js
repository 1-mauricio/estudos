class Meal {
    // == __init__
    constructor (food) {
        this.food = food
    }

    eat() {
        return 'ate'
    }
}

const carne = new Meal('carne')
console.log(carne)