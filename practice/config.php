<?php
$host = 'localhost';
$db_name = 'your_db_name';
$username = 'your_username';
$password = 'your_password';
$connection = new PDO('mysql:host=' . $host . ';dbname=' . $db_name, $username, $password);
?>
