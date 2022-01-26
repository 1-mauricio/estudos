let soma = (a,b) => {
    return a+b;
}

module.exports = soma

/* IMPORT */ 

let somaFunc = require('./soma')
console.assert(somaFunc(10,5) == 15)