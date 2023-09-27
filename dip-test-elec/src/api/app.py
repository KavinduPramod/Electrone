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
    register_number = db.Column (db.String(100), )
    username = db.Column(db.String(100),unique=True)
    password = db.Column(db.Integer,unique=True)

    User = db.relationship('User', backref='user')
 
class User_role(db.Model):
    __tablename__="user_role"
    id = db.Column(db.Integer, primary_key=True)
    user_role = db.Column (db.String(100))

    user_role_id = db.Column(db.Integer, db.ForeignKey('user_role.id'))

@app.route('/login_admin', methods=['POST'])
def login_admin():
    data = request.get_json()
    user_input_username = data.get('user_name')
    user_input_password = data.get('password')
    if not user_input_username or not user_input_password:
        return jsonify({"message": "Please enter both username and password"}), 401

    user = User.query.filter_by(user_name=user_input_username).first()
    if user:
        if user.user_role_id == 1:
            if user.password == user_input_password:                
                return jsonify({"message": "Login successful!"}), 200
            else:
                return jsonify({"message": "Incorrect password. Please check your input"}), 401
    
        if user.user_role_id == 2:
            if user.password == user_input_password:                
                return jsonify({"message": "Login successful!"}), 200
            else:
                return jsonify({"message": "Incorrect password. Please check your input"}), 401
        else:
            return jsonify({"message": "User does not have permission to log in"}), 403
    else:
        return jsonify({"message": "Invalid username. Please check your input"}), 401

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False) 