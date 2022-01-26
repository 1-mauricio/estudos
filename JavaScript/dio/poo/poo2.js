class Animal {
    constructor(type = "animal") {
        this.type = type;
    }

    get type() {
        return this._type;
    }

    set type(val) {
        this._type = val.toUpperCase();
    }

    makeSound() {
        console.log("Making animal sound");
    }
}

class Cat extends Animal {
    constructor() {
        super("cat");
    }

    // sobrescreve o makeSound da classe pai
    makeSound() {
        super.makeSound();
        console.log("Meow");
    }
}

// super() utiliza propriedades do construtor da classe pai

let b = new Cat();
console.log(b.makeSound());
