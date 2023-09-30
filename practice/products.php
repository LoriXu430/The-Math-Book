<?php
include 'config.php';

// Fetch products
$query = $connection->prepare("SELECT * FROM products");
$query->execute();
$products = $query->fetchAll();
?>

<!-- HTML to display products -->
<table border="1">
    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Price</th>
        </tr>
    </thead>
    <tbody>
        <?php foreach ($products as $product): ?>
        <tr>
            <td><?php echo $product['id']; ?></td>
            <td><?php echo $product['name']; ?></td>
            <td><?php echo $product['price']; ?></td>
        </tr>
        <?php endforeach; ?>
    </tbody>
</table>
