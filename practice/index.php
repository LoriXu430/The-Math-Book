<?php
require_once 'database.php';
require_once 'product.php';

use MyPHPApp\Database;
use MyPHPApp\Product;

$database = new Database();
$db = $database->connect();

$product = new Product($db);
$result = $product->read();

if ($result->rowCount()) {
    while ($row = $result->fetch(\PDO::FETCH_ASSOC)) {
        extract($row);
        $product_item = array(
            'id' => $id,
            'name' => $name,
            'price' => $price
        );
        echo "Product ID: " . $product_item['id'] . " Name: " . $product_item['name'] . " Price: $" . $product_item['price'] . "<br>";
    }
} else {
    echo "No products found!";
}