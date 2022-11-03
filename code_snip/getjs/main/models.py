#Main backend of the project. All the dealings with the database are defined here
from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import user_collection #import the other collection variables here
import uuid


class User:

    def start_session(self, user):
        print(user)
        del user['password']
        del user['_id']
        session['logged_in'] = True
        session['user'] = user
        print("okay till here")
        return jsonify(user), 200

    def signup(self):

        # print(request.form)

        #Fetch form details
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        contact = request.form.get('contact')
        password = request.form.get('password')
        cpass = request.form.get('confirmpass')
        # Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": name,
            "username": username,
            "email": email,
            "contact": contact,
            "password": password
        }
        print(user)

        #confirm password
        if password != cpass:
            return jsonify({"error": "Password Mismatch"}), 400

        # Check for existing email address
        if user_collection.find_one({"username": user['username']}):
            return jsonify({"error": "Username in use"}), 400
        
        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        if user_collection.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "Signup Unsuccessful"}), 400

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):
        print("reached here")
        username = request.form.get('username')
        password = request.form.get('password')
        user = user_collection.find_one({"username": username})
        print(user)

        if user and pbkdf2_sha256.verify(password, user['password']):
            return self.start_session(user)

        return jsonify({"error": "Invalid credentials"}), 401