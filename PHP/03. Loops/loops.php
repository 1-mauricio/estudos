<?php
    # LOOPS -Execute code set number of times
    
    /*
        For
        While
        Do.. While
        Foreach
    */

    # FOR
    /*
    for($i = 0; $i <= 10; $i++) {
        echo 'Number: ' .$i;
        echo '<br>';
    }
    */
    
    # WHILE
    /*
    $i = 0;
    while($i < 10){
        echo $i;
        echo '<br>';
        $i++;
    }
    */
    
    # DO WHILE
    /*
    $i = 0;

    do {
        echo $i;
        echo '<br>';
        $i++;
    }
    while($i < 10);
    */

    #FOREACH - For arrays

    $people = ['Brad' => 'brad@gmail', 'Jose' => 'jose@gmail', 'William' => 'william@gmail'];
    foreach($people as $person => $email){
        echo $person.': '.$email;
        echo '<br>';
    }
?>