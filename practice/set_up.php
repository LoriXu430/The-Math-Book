<?php
$db = new PDO('sqlite:messages.db');
$query = 'CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, user TEXT, message TEXT)';
$db->exec($query);
echo "Setup completed!";
