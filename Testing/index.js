class Person{
    constructor(name,city) {
        this.name = name
        this.city=city
    }
    greet() {
        return(`Hello, ${this.name} from ${this.city}`);
    }
}

const p1 = new Person('Dilip',"Nashik");
console.log(p1);
const greet = p1.greet();
console.log(greet);

module.exports = Person;