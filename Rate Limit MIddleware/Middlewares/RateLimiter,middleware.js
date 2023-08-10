
const rateLimit = (limit, time, blockedTime)=>{
    
    // to store the requests
    const requests = {};

    // create the interval

    setInterval(() => {
        
        // check each ip in requests
        for (const ip in requests) {
            const now = Date.now();

            // current time window
            const timeWindow = requests[ip].timeWindow;

            // blocket period

            const blockedUntill = requests[ip].blockedUntill;

            // remove the req older than timewindow
            requests[ip].requests = requests[ip].requests.filter((time) => {
                return time > now - timeWindow;
            })

            // if no requests present

            if (requests[ip].requests.length === 0) {
                requests[ip].timeWindow = now;
            }


            // reset count after the blockperiod ended
            if (blockedUntill && blockedUntill <= now) {
                requests[ip].blockedUntill = null;
                requests[ip].requests = [];
                requests[ip].timeWindow = now;
            }
        }
    }, time);

    // return the middleware

    return (req, res, next) => {
        const ip = req.ip;

        const now = Date.now();

        requests[ip] = requests[ip] || { requests: [], timeWindow: now };

        // if blocked for period
        if (requests[ip].blockedUntill && requests[ip].blockedUntill > now) {
            
            const remainingTime = Math.ceil((requests[ip].blockedUntill - now) / 1000);
            res
                .status(429)
                .send(
                    `Too many requests, please try again after ${remainingTime} seconds.`
                );
        }

        // if reached req limit
        else if (requests[ip].requests.length>=limit) {
            requests[ip].blockedUntill = now + blockedTime;

            const remainingTime = Math.ceil(blockedTime / 1000);
            res
                .status(429)
                .send(
                    `Too many requests, please try again after ${remainingTime} seconds.`
                );
        }
        else {
            requests[ip].requests.push(now);
            next();
        }
    }
}

module.exports=rateLimit