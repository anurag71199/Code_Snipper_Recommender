#Routes just calls User class methods from models.py upon receiving form values
from flask import Flask, render_template, redirect, url_for, request, session
from app import app
from main.models import User


@app.route('/register', methods=['POST'])
def signup():
    return User().signup()
    # return render_template('signup.html')


@app.route('/signout')
def signout():
    return User().signout()


@app.route('/login', methods=['POST'])
def login():
    print("reached login route")
    return User().login()

@app.route('/uploadsnip', methods=['POST'])
def upload():
    return User().upload()

# from flask import Blueprint, render_template, redirect, url_for, request, session
# from passlib.hash import pbkdf2_sha256

# from getjs.extensions import mongo

# main = Blueprint('main', __name__)


# def start_session(user):
#         del user['password']
#         session['logged_in'] = True
#         session['user'] = user
#         return

# @main.route('/')

# def index():
#     return render_template('index.html')

# @main.route('/userhome')
# def userhome():
#     return render_template('userhome.html')

# @main.route('/login')
# def loginnav():
#     return render_template('login.html')

# @main.route('/login', methods=['POST'])
# def login_user():
#     error = None
#     user_collection = mongo.db.users
#     username = request.form.get('username')
#     password = request.form.get('password')
    
#     user = user_collection.find_one({"username": username})
#     if user and pbkdf2_sha256.verify(password, user['password']):
#         start_session(user)
#         return render_template('userhome.html')
        
#     else:
#         print("mismatch creds")
#     return redirect(url_for('main.index'))



# @main.route('/register')
# def regnav():
#     return render_template('register.html')

# @main.route('/register', methods=['POST'])
# def add_user():
#     error = None
#     user_collection = mongo.db.users
#     name = request.form.get('name')
#     username = request.form.get('username')
#     email = request.form.get('email')
#     contact = request.form.get('contact')
#     password = request.form.get('password')
#     cpass = request.form.get('confirmpass')
    
#     if password != cpass:
#         print("pass mismatch") #alert message redirected to register page
#         error = 'Invalid credentials'
#     else:
#         passencrypt = pbkdf2_sha256.encrypt(password)
#         user_collection.insert_one({'name': name, 'username': username, 'email': email, 'contact': contact, 'password': passencrypt, 'type': 'user'})
#     return redirect(url_for('main.index'))
