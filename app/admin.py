from flask import Blueprint, request, jsonify
import os

admin_bp = Blueprint('admin', __name__)

@admin_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    if email == os.getenv("ADMIN_EMAIL") and password == os.getenv("ADMIN_PASSWORD"):
        return jsonify({"success": True, "message": "Logged in!"})
    return jsonify({"success": False, "message": "Invalid credentials"}), 401
