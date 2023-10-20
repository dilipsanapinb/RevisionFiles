// class ListNode {
//   constructor(data) {
//     this.data = data;
//     this.next = null;
//   }
// }

// var linkedList =function(arr) {
//   let head = null;
//   let tail = null;

//   for (let i = 0; i < arr.length; i++) {
//     let newNode = new ListNode(arr[i]);
//     if (head === null) {
//       head = newNode;
//       tail = newNode;
//     } else {
//       tail.next = newNode;
//       tail = newNode;
//     }
//   }

//   return head;
// }

// var arr = [1, 2, 3, 4, 5];
// console.log(linkedList(arr));

function greet(greetings,city) {
    console.log(`${greetings}, ${this.name} from ${city}`);
}
perosn = {
    name:"Dilip"
}

greet.call(perosn, "Hello", "Nashik");
greet.apply(perosn, ["Hiii..", "Pune"]);
const greetperson = greet.bind(perosn, "Namaste", "Delhi");

greetperson()