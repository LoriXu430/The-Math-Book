<?php
class UserView {
    public function showHome() {
        echo "<h1>Welcome!</h1><a href='?action=register'>Register</a>";
    }

    public function showRegistrationForm() {
        echo "
        <h1>Register</h1>
        <form action='?action=store' method='post'>
            Username: <input type='text' name='username'><br>
            Password: <input type='password' name='password'><br>
            <input type='submit' value='Register'>
        </form>";
    }

    public function showSuccess() {
        echo "<h1>Success!</h1><a href='index.php'>Home</a>";
    }
}
