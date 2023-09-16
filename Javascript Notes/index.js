
// function sayHello() {
//         let name = 'Dilip';
//         function printName() {
//                 console.log(name);
//         };
//         printName();
// };
// sayHello();

// function makeAdded(x) {
//         return function (y) {
//                 return x+y
//         }
// }

// const add5 = makeAdded(5);
// const add10 = makeAdded(10);

// console.log(add5(2));
// console.log(add10(2));

function printFactorial(num) {
        if (num <= 1) {
                return 1
        } else {
                return num*printFactorial(num-1)
        }
}

let x = printFactorial(5);
console.log(x);
