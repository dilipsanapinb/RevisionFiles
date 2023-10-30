const myEventTarget = new EventTarget();

const myEvent = new Event('myEvent');

myEventTarget.addEventListener('myEvent', () => {
    console.log('Custom Event triggered');
});

myEventTarget.dispatchEvent(myEvent)