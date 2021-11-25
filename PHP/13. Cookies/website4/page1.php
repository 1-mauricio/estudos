<?php 
    if (isset($_POST['submit'])) {
        $username = htmlentities($_POST['username']);

        // (name of the cookie, value, expiration)
        setcookie('username', $username, time()+3600);
        //1 hour

        header('Location: page2.php');
    }


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="POST" action="<?php echo $_SERVER['PHP_SELF']; ?>">
        <input type="text" name="username" placeholder="enter username">
        <br>
        <input type="submit" name="submit" value="submit">
    </form>
</body>
</html>