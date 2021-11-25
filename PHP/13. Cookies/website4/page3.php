<?php 
    $user = ['name' => 'Maurício', 'email' => 'teste@teste.com', 'age' => 19];

    $user = serialize($user);

    setcookie('user', $user, time() + (86400 * 30));
    //1 day

    $user = unserialize($_COOKIE['user']);
    echo $user['name'];
?>