// String, Numbers, Boolean, null, undefined

const name = 'John';
const age = 30;
const rating = 4.5;
const isCool = true;
const x = null;
const y = undefined;
let z; //undefined

console.log(typeof z);

//STRING

//Concatenation
console.log('My name is ' + name +' and i am ' + age);
//Template String
console.log('My name is `${name} and i am ${age}`');
const hello = 'My name is ${name} and i am ${age}';
console.log(hello)


const s = 'Hello World';
const n = 'technology, computers, it, code';


console.log(s.length);
console.log(s.toUpperCase());
console.log(s.toLowerCase());
console.log(s.substring(0, 5).toUpperCase())
console.log(n.split(','));