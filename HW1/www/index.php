<?php

//error_reporting(E_ALL);

echo("Hola, APACHE 2 ! <br>");

$link=mysqli_connect('mysql','root','secret1234','miflib');

if($link==false) {

    printf("Cant open DATDBASE %s ",mysqli_connect_errno());
    phpinfo();
    exit();
}
else {
    printf("Database ok  <br>");
}

$sql = 'SELECT id, name, surname  FROM user_list';

$result = mysqli_query($link, $sql);

while ($row = mysqli_fetch_array($result)) {
    printf("NAME " . $row['name'] . "; ID. " . $row['id'] . " SURNAME ".$row['surname']. "<br>");
}

phpinfo();
?>
