
const request = require('request');


const url = ' https://quotes.rest/qod';

request({url:url},(error,response) => {
    let data = JSON.parse(response.body);
    console.log(JSON.stringify(data.contents.quotes[0].quote));
    });