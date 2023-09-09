class Myclass{
    constructor(name,city) {
        this.name = name
        this.city=city
    }
    greet() {
        return `Hello ${this.name} from ${this.city}!`
    }
}

const p1 = new Myclass('Dilip', 'Nasik');
console.log(p1);
console.log(p1.greet());

module.exports=Myclass