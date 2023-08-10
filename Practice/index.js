const { error } = require('console');
const https = require('https');

const options = {
    hostname: "aws.api.com",
    path: '/users',
    method: "GET",
    headers: {
        'Content-Type':'application/json'
    }
}

// callback function

const req = https.request(options, (res) => {
    let data = "";
    res.on('data', (chunk) => {
        data += chunk;
    });
    res.on('end', () => {
        console.log(data);
    });
});

req, on('error', (error) => {
    console.log(error);
})