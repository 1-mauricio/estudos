<?php
    # CONDITIONALS

    /*
        == only value
        === value and data type
        <
        >
        <=
        >=
        !=
        !==
    */

    /*
    $num = '5';
    if($num === 5){
        echo "5 passed";
    } else if($num === 6){
        echo '6 passed';
    } else {
        echo 'did not pass';
    }
    */

    
    $num = 5;
    /*
    if($num > 4) {
        if($num < 10){
            echo "$num passed";
        } else {
            echo 'whatever';
        }
    }
    */

    /*
        Logical

        and &&
        or ||
        xor
    */

    if($num > 4 AND $num < 10){
        echo "$num passed";
    } 

    if($num > 4 OR $num < 10){
        echo "$num passed";
    } 

    if($num > 4 XOR $num < 10){
        echo "$num passed";
    } 

    # SWITCH

    $favColor = 'red';

    switch($favColor) {
        case 'red':
            echo 'Your favorite color is red';
            break;
        case 'blue':
            echo 'Your favorite color is blue';
            break;
        default:
            echo 'Your favorite color is something else';
    }

?>