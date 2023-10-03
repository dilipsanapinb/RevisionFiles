const { response } = require('express');
const http = require('http');

const server = http.createServer((request, response) => {
    if (request.url == "/") {
        response.end("Welcome, this is a basic route for the app")
    }
    else if (request.url == "/user") {
        response.end("This is a user route")
    }
});


server.listen(5000, () => {
    console.log('Server is running on port:5000');
})