from flask import Flask, request, jsonify, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from flask_principal import Principal, Permission, RoleNeed

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

login_manager = LoginManager(app)
principal = Principal(app)

admin_permission = Permission(RoleNeed('admin'))

class User(UserMixin):
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

users = [User(1, 'user', 'admin'), User(2, 'user2', 'user')]

@login_manager.user_loader
def load_user(user_id):
    return next((user for user in users if user.id == int(user_id)), None)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    user = next((user for user in users if user.username == username), None)
    if user:
        login_user(user)
        return redirect(url_for('profile'))
    return jsonify({'message': 'Invalid username'}), 401

@app.route('/profile')
@login_required
def profile():
    return jsonify({'message': 'This is a protected route', 'user': current_user.username})

@app.route('/admin')
@login_required
@admin_permission.require(http_exception=403)
def admin():
    return jsonify({'message': 'This is an admin protected route'})

if __name__ == '__main__':
    app.run(port=3000)
