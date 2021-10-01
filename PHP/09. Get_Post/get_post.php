<?php
    
    if (isset($_GET['name'])) {
        $name = htmlentities($_GET['name']);
        //echo $name;


        // htmlentities evita que se coloquem tags html
        //echo $_GET['email'];
    }
    /*
    if(isset($_POST['name'])) {
        $name = htmlentities($_POST['name']);
    }
    */

    /*

    if(isset($_REQUEST['name'])) {
        $name = htmlentities($_REQUEST['name']);
        echo $name;
    }
    
    echo $_SERVER['QUERY_STRING'];
    */
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
</head>
<body>
    <form method="GET" action="get_post.php">
        <div>
            <label>Name</label><br>
            <input type="text" name="name">
        </div>
        <div>
            <label>Email</label><br>
            <input type="text" name="email">
        </div>
        <input type="submit" value="submit">
    </form>

    <ul>
        <li>
            <a href="get_post.php?name=Mauricio">Mauricio</a>
        </li>
        <li>
            <a href="get_post.php?name=Brad">Brad</a>
        </li>
    </ul>

    <h1><?php echo "{$name}'s Profile"; ?> </h1>
</body>
</html>