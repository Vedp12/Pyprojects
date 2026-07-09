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
from flask_sqlalchemy import SQLAlchemy  
from sqlalchemy.exc import IntegrityError

import os
from environs import Env
from datetime import timedelta

env = Env()
env.read_env()
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'bank_auth.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["JWT_SECRET_KEY"] = env("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)

jwt = JWTManager(app)
db = SQLAlchemy(app)

# with app.app_context():
#     db.create_all()
#     print("database created")

class Authentication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(260), nullable=False)


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "data is not in json format"}), 400
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    if not name or not email or not password:
        return jsonify({"error": "All field are required"}), 400
    # "@gmail" or "@yahoo" or "Outlook" or "@tuta"
    if "@" not in email:
        return jsonify({"error": "email is incorrect"}), 400
    if not name.strip():
        return jsonify({"error": "name not be empty!"})
    if Authentication.query.filter_by(email=email).first():
        return jsonify({"error": "mail already exist "})
    
    HashedPassword = generate_password_hash(password)
    new_auth = Authentication(name=name, email=email, password=HashedPassword)
    
    try:
        db.session.add(new_auth)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "email already exists"}), 409
    except Exception:
        return jsonify({"error":"something went wrong"}),400
    return jsonify({"success":"user created successfully"}),201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "data is not in json format"})
    # name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "All field are required"}), 400

    mail = Authentication.query.filter_by(email=email).first()

    if "@" not in email:
        return jsonify({"error": "email is incorrect"}), 400
    if not mail or not check_password_hash(mail.password, password):
        return jsonify({"error": "email or password is incorrect "}), 401

    access_token = create_access_token(identity=email)
    refresh_token = create_refresh_token(identity=email)
    return jsonify({"access_token": access_token, "refresh_token": refresh_token})


if __name__ == "__main__":
    app.run(port="5002")