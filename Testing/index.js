const person = {
  name: "John",
  age: 30,
  address: {
    street: "123 Main St",
    city: "New York",
    country: "USA",
  },
};

// Destructuring nested objects
const {
  name,
  age,
  address: { city, country },
} = person;

console.log(name); // Output: John
console.log(age); // Output: 30
console.log(city); // Output: New York
console.log(country);
