<?php
    // single line comment
    # ""
    /*
        multiline comment
    */
    /*
        - Prefix $
        - Star with a letter or an underscore
        - only letters, numbers and underscores
        - case sensitive
    */
    /* DATA TYPES
        String
        Integers
        Floats
        booleans
        Array
        Objects
        NULL 
        Resource
    */

    $output = 'Hello World';

    $num1 = 4;
    $num2 = 10;
    $sum = $num1 + $num2;

    $string1 = 'Hello';
    $string2 = 'World';
    $greeting = $string1 . ' ' . $string2;
    $greeting2 = "$string1 $string2";

    $string3 = 'They\'re Here';
    $string4 = "They're Here";
    
    $float1 = 4.4;
    $bool1 = true;

    //CONSTANT
    define('GREETING', 'Hello Everyone');


    echo GREETING;
?>