from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt,
    get_jwt_identity,
)
import os
from environs import Env
from datetime import timedelta

# load_dotenv()
env = Env()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = (
    "KlWRSoyb1CwI45SB0-wQYBD2FTBb_A"  # move to env var in real use
)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)

jwt = JWTManager(app)

user_db = {}
BLOCKLIST = set()


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON data required"}), 400
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    if not username or not email or not password:
        return jsonify({"error": "all fields are required"}), 400
    if "@" not in email:
        return jsonify({"error": "something wrong with email"}), 400
    if not username.strip():
        return jsonify({"error": "Username cannot be empty"}), 400
    if username in user_db:
        return jsonify({"error": "Username already exist"}), 400

    hashed_password = generate_password_hash(password)
    user_db[username] = {"email": email, "password": hashed_password}
    return jsonify({"success": f"{username} created successfull"})


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON data required"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "all fields are required"}), 400
    user = user_db.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "username or password is incorrect"}), 401

    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)

    return jsonify(access_token=access_token, refresh_token=refresh_token), 200


@app.route("/logout", methods=["DELETE"])
@jwt_required
def logout():
    jti = get_jwt["jti"]
    BLOCKLIST.add(jti)
    return jsonify({"msg": "successfully logout"}), 200


@app.route("/refresh", methods=["POST"])
def refresh():
    identity = get_jwt_identity()
    new_access_token = create_access_token(identity=identity)
    return jsonify(access_token=new_access_token), 200


app.route("/protected", methods=["GET"])


@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"success": f"User logged in as {current_user}"}), 200


if __name__ == "__main__":
    app.run(port="5001")
