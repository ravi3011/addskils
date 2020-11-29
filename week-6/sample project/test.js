let promise = new Promise(function (resolve, reject){
    reject(2);
}).catch();
// .then(
//     function(result){
//         console.log(result);
//     },
//     function(error){
//         return error;
//     }
// ).then(
//     function(error){
//         console.log("Result: "+ error);
//     }
// )