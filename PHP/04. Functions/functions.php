<?php
    # FUNCTIONS - Block of code that can be repeatedly called

    /*
        Camel Case - myFunction()
        Lower Case - my_function()
        Pascal Case - MyFunction()
    */

    /*
    function simpleFunction(){
        echo 'Hello World';
    }

    simpleFunction();
    */

    /*
    function sayHello($name = 'World') {
        echo "Hello, $name<br>";
    }

    sayHello('Mauricio');
    sayHello();
    */

    function addNumbers($num1, $num2){
        return $num1 + $num2;
    }

    $soma = addNumbers(2,3);
    echo "$soma<br>";

    // By Reference
    
    $myNum = 10;

    function addFive($num){
        $num += 5; 
    }

    function addTen(&$num){
        $num += 10;
    }

    addFive($myNum);
    echo "Value: $myNum<br>"; //doesn't change

    addTen($myNum);
    echo "value: $myNum<br>" //changes to 20
?>