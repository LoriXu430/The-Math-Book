<?php
$db = new PDO('sqlite:messages.db');
$stmt = $db->query('SELECT * FROM messages ORDER BY id DESC');
$messages = $stmt->fetchAll(PDO::FETCH_OBJ);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Messages</title>
</head>
<body>
    <h1>Messages</h1>
    <?php foreach ($messages as $message): ?>
    <div>
        <strong><?php echo htmlspecialchars($message->user); ?>:</strong>
        <p><?php echo htmlspecialchars($message->message); ?></p>
    </div>
    <?php endforeach; ?>
    <a href="submit.php">Submit a new message</a>
</body>
</html>
