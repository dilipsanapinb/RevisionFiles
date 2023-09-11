const express = require('express');
const app = express();

const httpServer = require('http').createServer(app);

const msgLimit = 10;

const clientMsgCounts = new Map();


// msg ratelimit middleware;

const rateLimitMiddleware = (socket, next) => {
    const clinetId = socket.id;
    const currTime = Date.now();

    if (!clientMsgCounts.has(clinetId)) {
        clientMsgCounts.set(clinetId, {
            count: 1,
            lastMsgTime: currTime,
        });
    } else {
        const clientInfo = clientMsgCounts.get(clinetId);

        const elapsedTime = currTime - clientInfo.lastMsgTime;

        if (elapsedTime < 10000) {
            if (clientInfo.count <= msgLimit) {
                return next(new Error("Message rate limit exceeded"));
            } else {
                clientInfo.count++;
                clientInfo.lastMsgTime = currTime;

            }
        } else {
            clientInfo.count = 1;
            clientInfo.lastMsgTime = currTime;
        }
    }
    next();
}

const {Server}= require('socket.io');
const io=new Server(httpServer)
app.get('/', (req, res) => {
    res.sendFile(__dirname+'/index.html')
})

io.on('connection', (socket) => {
    console.log(`Connected to server:${socket.id}`);

    socket.use(rateLimitMiddleware);

    socket.on('msg', (msg) => {
        io.emit('msg',msg)
    })
    socket.emit('msg',);

    socket.on("disconnect", () => {
        console.log(`Scoket disconected :${socket.id}`);
    });
});


httpServer.listen(8002, () => {
    console.log('Server is listening to port 8002');
})