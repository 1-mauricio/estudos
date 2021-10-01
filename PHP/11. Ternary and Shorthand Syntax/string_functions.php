<?php 
    # substr()
    # Return a portion of a string

    /*
    $output = substr('Hello', 1, 3);
    $output = substr('Hello', -2);
    echo $output;
    */

    # strlen()
    # Returns the length of a string

    /*
    $output = strlen('Hello World');
    echo $output;
    */

    # strpo()
    # finds the position of the first accurence of a sub string

    /*
    $output = strpos('Hello World', 'o');
    echo $output;
    */

    # strrpo()
    # finds the position of the last accurence of a sub string

    /*
    $output = strpos('Hello World', 'o');
    echo $output;
    */

    # trim()
    # Strips whitespace

    /*
    $text = 'Hello World              ';
    var_dump($text);

    $trimmed = trim($text);
    var_dump($trimmed);
    */

    # strtoupper
    # makes everythin uppercase

    /*
    $output = strtoupper('Hello World');
    echo $output;
    */

    # strtolower
    # makes everythin lowercase

    /*
    $output = strtoupper('Hello World');
    echo $output;
    */

    #ucwords()
    # capitalize every word

    /*
    $output = ucwords('hello world');
    echo $output;
    */

    # str_replace()
    # Replace all occurences of a search string with a replacement

    /*
    $text = 'Hello World';
    $output = str_replace('World', 'Everyone', $text);
    echo $output;
    */

    # is_string()
    # Check if string

    /*
    $val = '22';
    $output = is_string($val);

    echo $output;
    

    $values = array(true, false, null, 'abc', 33, '33', 22.4, '22.4', '', ' ', 0, '0');

    foreach($values as $value) {
        if(is_string($value)) {
            echo "{$value} is a string<br>";
        }
    }
    */

    #gzcompress()
    # Compress a string

    /*
    $string = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto quod excepturi deleniti corporis? Incidunt rerum dolorem repudiandae minus tempore adipisci accusantium! Perferendis, ratione accusamus dicta quam non natus dolores reprehenderit.";

    $compressed = gzcompress($string);

    echo $compressed;

    $original = gzuncompress($compressed);

    echo $original;
    */

?>