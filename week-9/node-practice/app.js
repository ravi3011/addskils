
var http = require('http');
var fs =  require('fs');

http.createServer((req,res) =>{
    res.writeHead(200,{'Content-Type': 'application/json'});
    var obj = {
        firstname:"john",
        lastname: "doe"
    };
    res.end(JSON.stringify(obj));
}).listen(3030,(error) =>{
    console.log(error);
});

// http.createServer((req,res) =>{
//     res.writeHead(200,{'Content-Type': 'text/html'});
//     fs.createReadStream(__dirname + '/index.html').pipe(res);

// }).listen(3030,(error) =>{
//     console.log(error);
// });


// var http = require('http');
// var fs =  require('fs');

// http.createServer((req,res) =>{
//     res.writeHead(200,{'Content-Type': 'text/html'});
//     var html = fs.readFileSync(__dirname + '/index.html','utf-8');
//     var message = "Hello world...";
//     html = html.replace('{Message}',message);
//     res.end(html);
// }).listen(3030,(error) =>{
//     console.log(error);
// });


// var fs = require('fs');
// var fs = require('fs/promises');

// (async (path) => {
//     try{
//         await fs.unlink(path);
//         console.log(`succesfully deleted ${path}`);
//     }catch (error){
//         console.log(`there was no directory or file woth name ${error.message} `);
//     }
// })('hello');





// fs.unlink('hello',(err) => {
//     if(err) throw err;
//     console.log('successfully deleted hello')
// });

// var greet = fs.readFileSync(__dirname+"/test.text",'utf8');
// console.log(greet);

// var con = fs.readFile(__dirname+"/test.text",'utf8',( err , data) =>{
//     console.log(data);
// });

// console.log("last line")



// function print(s){
//     console.log(s);
// }

// function main(anotherFunction,value){
//     anotherFunction(value);
// }

// main(print,"Hello word!");

// console.log(__filename);
// console.log(__dirname);

// setTimeout(()=>{
//     console.log("this is set time out");
// },3000);
// setInterval(()=>{
//     console.log("this is set interval");
// },3000);


// 'use strict';

// class Person{
//     constructor(firstname,lastname){
//         this.firstname = firstname;
//         this.lastname = lastname;
//     }

//     greet(){
//         console.log("hello," + this.firstname +" "+this.lastname);
//     }
// }

// var john = new Person("johan","kumar");
// john.greet();


// var buf = new Buffer('Hello word', 'utf8');

// console.log(buf);
// console.log(buf.toJSON());