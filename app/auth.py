# app/auth.py
from flask import request, jsonify

TOKEN = "secure_token"

def token_required(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token != TOKEN:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return wrapper

