<?php
namespace MyPHPApp;

class Product {
    private $conn;
    private $table = 'products';

    public $id;
    public $name;
    public $price;

    public function __construct($db) {
        $this->conn = $db;
    }

    public function read() {
        $query = 'SELECT * FROM ' . $this->table;
        $stmt = $this->conn->prepare($query);
        $stmt->execute();

        return $stmt;
    }
}