// const http = requre('http');

// const options = {
//     hostname: "http://localhost:8000",
//     port: 8000,
//     path: '/',
//     method: "GET",
//     headers: {
//         "Content-Type": "application/json",
//         "Authorisation": "Bearer token"
//     },
// };

// const req = http.request(options, (res) => {
//     console.log(`Status code:${res.statusCode}`);
// })



function setIterval(func,delay,...args){
    function interval() {
        func.apply(null, args);
        setTimeout(interval,delay)
    }
    setTimeout(interval,delay)
}

function sayHello() {
    console.log('Hello');
}

setIterval(sayHello,1000)