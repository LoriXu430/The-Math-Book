<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['user'], $_POST['message'])) {
    $db = new PDO('sqlite:messages.db');
    $stmt = $db->prepare('INSERT INTO messages (user, message) VALUES (?, ?)');
    $stmt->execute([$_POST['user'], $_POST['message']]);
    echo "Message submitted!";
} else {
?>
<form action="submit.php" method="post">
    Name: <input type="text" name="user"><br>
    Message: <textarea name="message"></textarea><br>
    <input type="submit" value="Submit">
</form>
<?php } ?>
