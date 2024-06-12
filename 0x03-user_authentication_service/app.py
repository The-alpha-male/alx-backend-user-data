#!/usr/bin/env python3
"""Basic Flask application"""
from flask import Flask, jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'])
def users() -> str:
    """"Users post method"""
    email = request.form.get('password')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
