#Routes just calls User class methods from models.py upon receiving form values
from flask import Flask, render_template, redirect, url_for, request, session
from app import app
from main.models import User


@app.route('/register', methods=['POST'])
def signup():
    return User().signup()


@app.route('/signout')
def signout():
    return User().signout()


@app.route('/login', methods=['POST'])
def login():
    print("reached login route")
    return User().login()

@app.route('/uploadsnip', methods=['POST'])
def upload():
    return 