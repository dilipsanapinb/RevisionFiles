
const { expect } = require('chai');
const Myclass = require('./index');
describe('Myclass', () => {

    // check new instace
    it('should create a new instance with the name', () => {
        const name = 'Dilip';
        const city = 'Nasik';
        const person = new Myclass(name, city);
        expect(person).to.be.an.instanceOf(Myclass);
        expect(person.name).to.equal(name);
        expect(person.city).to.equal(city);
    });

    // check the greet method
    it('shoud return correct greeting message', () => {
        const name = "Dilip";
        const city = "Nasik";
        const person = new Myclass(name, city);
        const greeting = person.greet();
        expect(greeting).to.equal(`Hello ${name} from ${city}!`);
    })
})

