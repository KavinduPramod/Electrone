from __init__ import app, db



if __name__ == '__main__':
    from models import  User,User_role
    with app.app_context():
        db.create_all()
    app.run(debug=False) 