<?php
require_once 'controllers/UserController.php';

$action = $_GET['action'] ?? 'home';

$controller = new UserController();

switch($action) {
    case 'register':
        $controller->register();
        break;
    case 'store':
        $controller->store();
        break;
    default:
        $controller->index();
}
