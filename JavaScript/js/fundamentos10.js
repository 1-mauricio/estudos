function addNums(num1 = 1, num2 = 2) {
    return num1 + num2;
}

const addNums = (num1 = 1, num2 = 2) => console.log(num1 + num2);

//overwrite
console.log(addNums(5,5));

