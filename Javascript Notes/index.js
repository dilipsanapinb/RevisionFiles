
var arr=[1,2,3,4,5]
for (var i = 0; i < arr.length; i++){
    (function (i) {
        setTimeout(function () {
            console.log(arr[i], i);
        },i*1000)
    })(i)
}