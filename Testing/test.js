const { expect } = require('chai');

const Person = require("./index");

describe('Person', () => {
    it ('sjould create new instance with the person name and city', () => {
        const name = 'Dilip';
        const city = 'Nashik';
        const person = new Person(name, city);
        expect(person).to.be.an.instanceOf(Person);
        expect(person.name).to.equal(name)
        expect(person.city).to.equal(city)
    })

    // greeting
    it('should return correct greeting message', () => {
        const name = 'Dilip';
        const city = 'Nashik';
        const person = new Person(name, city);
        const greeting = person.greet();
        expect(greeting).to.equal(`Hello, ${name} from ${city}`);
    })
})
