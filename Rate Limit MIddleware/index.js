const express = require('express');
const rateLimit = require('./Middlewares/RateLimiter,middleware');

const app = express();

app.get('/user',rateLimit(5,60*1000,30*1000), (req, res) => {
    res.status(200).json({message:"Users data"})
})

app.listen(5000, () => {
    console.log('Server is running on port 5000');
})