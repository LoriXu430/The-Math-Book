<?php
require_once 'models/User.php';
require_once 'views/UserView.php';

class UserController {
    private $view;

    public function __construct() {
        $this->view = new UserView();
    }

    public function index() {
        $this->view->showHome();
    }

    public function register() {
        $this->view->showRegistrationForm();
    }

    public function store() {
        $user = new User($_POST['username'], password_hash($_POST['password'], PASSWORD_DEFAULT));
        // You'd typically save this user object to a database here
        $this->view->showSuccess();
    }
}
