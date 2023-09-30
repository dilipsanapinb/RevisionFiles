function prtinHello(time) {
    return new Promise((res, rej) => {
        if (typeof (time) !== 'number') {
            rej('assignment of function should be a number')
        }
        return;
        setTimeout(() => {
            res({ status: 200 });
        }, time);
    })
}
prtinHello(2000)
    .then(res => console.log('printed after 2s'))
    .catch(err => console.log(err));
