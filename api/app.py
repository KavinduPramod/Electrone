from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

DB_NAME = "TEST__DB"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}.db'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    register_number = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))  # Change the data type to String

    # Define a foreign key relationship to User_role
    user_role_id = db.Column(db.Integer, db.ForeignKey('user_role.id'))

class User_role(db.Model):
    __tablename__ = "user_role"
    id = db.Column(db.Integer, primary_key=True)
    user_role = db.Column(db.String(100))

@app.route('/login_admin', methods=['POST'])
def login_admin():
    data = request.get_json()
    user_input_username = data.get('user_name')
    user_input_password = data.get('password')
    if not user_input_username or not user_input_password:
        return jsonify({"message": "Please enter both username and password"}), 401

    user = User.query.filter_by(username=user_input_username).first()

    if user:
        if user.user_role_id == 1:
            if user.password == user_input_password:
                return jsonify({"message": "Login successful!"}), 200
            else:
                return jsonify({"message": "Incorrect password. Please check your input"}), 401
        else:
            return jsonify({"message": "No access"}), 403
    else:
        return jsonify({"message": "Invalid username. Please check your input"}), 401
    
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    register_number = data.get('register_number')
    username = data.get('username')
    password = data.get('password')
    user_role_id = data.get('user_role_id')

    if not register_number or not username or not password:
        return jsonify({"message": "Please provide all required user data"}), 400

    # Check if the username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"}), 409

    # Create a new user instance and add it to the database
    new_user = User(register_number=register_number, username=username, password=password, user_role_id=user_role_id)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User added successfully"}), 201

@app.route('/add_user_role', methods=['POST'])
def add_user_role():
    data = request.get_json()
    user_role_name = data.get('user_role')

    if not user_role_name:
        return jsonify({"message": "Please provide the user role name"}), 400

    # Check if the user role already exists
    if User_role.query.filter_by(user_role=user_role_name).first():
        return jsonify({"message": "User role already exists"}), 409

    # Create a new user role instance and add it to the database
    new_user_role = User_role(user_role=user_role_name)
    db.session.add(new_user_role)
    db.session.commit()

    return jsonify({"message": "User role added successfully"}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False) 