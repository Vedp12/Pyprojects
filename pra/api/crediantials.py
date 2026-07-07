from flask import Flask, jsonify, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
import datetime

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "KlWRSoyb1CwI45SB0-wQYBD2FTBb_A"

jwt = JWTManager(app)

users_db = {}


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Json data required"}), 400
    username = data.get("username")
    password = data.get("password")
    user = users_db.get(username)
    if not username or not password:
        return jsonify({"error": "Both username and password field required!"})
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Username or password is incorrect"}), 401
    # access_token = create_access_token(identity=username)
    token = jwt.encode(
        {"user": username, "exp": datetime.utcnow() + datetime.timedelta(minute=2)},
        app.config["SECRET_KEY"],
        algorithm="HS256",
    )
    return jsonify(token=token)


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Json data required"}), 400

    username = data.get("username")
    email = data.get("email")
    age = data.get("age")
    password = data.get("password")
    if not username or not email or not age or not password:
        return jsonify({"error": "all field are required"})
    if not isinstance(age, int):
        return jsonify("error", "age must be int")
    if not username.strip():
        return jsonify({"msg": "Username not be empty"})
    if username in users_db:
        return jsonify({"msg": "User already exists"}), 400
    hashed_password = generate_password_hash(password)
    users_db[username] = {"email": email, "age": age, "password": hashed_password}
    return jsonify({"msg": "User created successfully", "username": username}), 201


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


@app.route("/protected", methods=["GET"])
@jwt_required()
def home():
    current_user = get_jwt_identity()
    return jsonify({"success": f"User logged in as {current_user}"}), 200


if __name__ == "__main__":
    app.run(debug=True)
