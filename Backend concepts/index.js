const myEventTarget = new EventTarget();

const myEvent = new Event('myEvent');

myEventTarget.addEventListener('myEvent', function (event) {
  console.log('Custom event triggred');
})

myEventTarget.dispatchEvent(myEvent);