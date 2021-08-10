//ARRAYS - variable that hold multiple values

const fruits = ['apples', 'oranges', 'pears', 10, true];
const numbers = new Array(1,2,3,4,5);

fruits[3] = 'grapes'; //pode adicionar, não pode fruits = []

fruits.push('mangos'); //adicionar ultimo
fruits.unshift('strawberries'); //adicionar primeiro

fruits.pop(); //exclui o ultimo

console.log(Array.isArray('hello'));

console.log(fruits.indexOf('oranges'))

console.log(numbers)
console.log(fruits)
console.log(fruits[3])