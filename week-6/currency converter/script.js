
var baseCurrency = "USD";

var baseNumber = 1;

var targetCurrency = "INR";

var targetNumber;

var url;


currencyConverter(baseCurrency,baseNumber,targetCurrency,targetNumber);


function currencyConverter(baseCurrency,baseNumber,targetCurrency,targetNumber){

    url = "https://api.exchangeratesapi.io/latest?symbols="+targetCurrency+"&base="+baseCurrency;
    $.get(url,function(data){
        console.log(data);
    })

}

