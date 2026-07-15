from contextlib import redirect_stdout
from types import NoneType

from flask import Flask, jsonify, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt,
    get_jwt_identity,
)
from sqlalchemy.exc import IntegrityError
import os

from environs import Env
from datetime import timedelta
from models import *
from functools import wraps

env = Env()
env.read_env()
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLAlchemy_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir,'bank.db')}"

app.config["SQLAlchemy_TRACK_MODIFICATIONS"] = True

try:
    app.config["JWT_SECRET_KEY"] = env.str("JWT_STR_KEY")
except Exception:
    app.config["JWT_SECRET_KEY"] = (
        "5Y4E3rlhAWL83q883ru5DwVUYpjglBU4FsJAMFWEqLs1e52ZJZuxrB3d64uYKbC77IttdMXv6KxdtnrMSw000cNdKkJWZCNxxaxV3WSIUcIEFFuxjeMKbKGjTwtWkF4F8stEF8QspWsyb5bCSsPZQPwPG"
    )

finally:
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=20)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)

db = SQLAlchemy(app)

# * Refresh
@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify({"access_token": new_access_token}), 200


# * Logout all
# @app.route('/logout',methods=["DELETE"])
# @jwt_required
# def logout():
#     jti = get_jwt("jti")


# *Admin required decorator
def admin_required():
    def wrapper():
        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):
            claims = get_jwt()
            if claims.get("is_admin") is True:
                return fn(*args, **kwargs)
            else:
                return jsonify({"msg": "admin only"}), 403
            return decorator

        return wrapper


# *Admin
# ? Signup
@app.route("/admin_sigup", methods=["POST"])
def admin_signup():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Data is not in json format"}), 401
    admin_name = data.get("admin_name")
    admin_email = data.get("admin_email")
    admin_password = data.get("admin_password")
    if not admin_name or not admin_email or not admin_password:
        return jsonify({"error": "all field are required"}), 400
    email_list = ["@gmail", "@yahoo", "@tuka", "@outlook"]
    if not any(email_list) in email:
        return f"email format is wrong use only: {[email_lists for email_lists in email_list]}"
    if not admin_name.strip():
        return jsonify({"error": "name not be empty"}), 400
    if Admin_login.query.filter_by(admin_email=admin_email).first():
        return jsonify({"error": "Email already exist"}), 400

    HashedPassword = generate_password_hash(admin_password)
    new_admin_auth = Admin_login(
        admin_name=admin_name, admin_email=admin_email, admin_password=HashedPassword
    )
    try:
        db.session.add(new_admin_auth)
        db.session.commit()
        access_token = create_access_token(identity=admin_email)
        refresh_token = create_refresh_token(identity=admin_email)
        return (
            jsonify(
                {
                    "Success": {
                        {"Access token": access_token},
                        {"Refresh token": refresh_token},
                    }
                }
            ),
            201,
        )
    except Exception:
        return jsonify({"error": Exception}), 400


# ? Login
@app.route("/admin_login", methods=["POST"])
def admin_login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Data is not in json format"}), 401
    admin_email = data.get("admin_email")
    admin_password = data.get("admin_password")
    if not admin_email or not admin_password:
        return jsonify({"error": "all field are required"}), 400

    user = Admin_login.query.filter_by(admin_email=admin_email).first
    email_list = ["@gmail", "@yahoo", "@tuka", "@outlook"]
    if not any(email_list) in email:
        return f"email format is wrong use only: {[email_lists for email_lists in email_list]}"
    if not user or not check_password_hash(user.admin_password, admin_password):
        return jsonify({"error" "email or password is incorrect"}), 401
    access_token = create_access_token(identity=admin_email)
    refresh_token = create_refresh_token(identity=admin_email)
    return (
        jsonify(
            {
                "Success": {
                    {"Access token": access_token},
                    {"Refresh token": refresh_token},
                }
            }
        ),
        201,
    )


# * Bank post
@app.route("/bank", methods=["POST"])
@admin_required
def create_bank():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Data is not in json format"}), 401
    bank_name = data.get("bank_name")
    bank_address = data.get("bank_address")
    admin_id = Admin_login.query.get(data["id"])

    if not bank_name or not bank_address or not admin_id:
        return jsonify({"error": "all field are required"}), 400
    if admin_id is None:
        return jsonify({"error": "Admin id does not exist"}), 404

    newBank = Bank(bank_name=bank_name, bank_address=bank_address, admin_id=admin_id)
    try:
        db.session.add(newBank)
        db.session.commit()
        return jsonify({"success": "Bank created successfully"}), 201
    except Exception:
        return jsonify({"error": Exception})


# * User Signup
@app.route("/user_signup", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Data is not in json format"}), 400
    user_name = data.get("user_name")
    user_age = data.get("user_age")
    user_email = data.get("user_email")
    user_password = data.get("user_password")
    # bank_id = Bank.query.get(data["id"])
    user_pin = data.get("user_pin")

    if bank_id is None:
        return jsonify({"error": "Bank id does not exist"}), 404

    if not user_name or not user_age or not user_email or not user_password or not user_pin:
        return jsonify({"error": "All field are required"}), 400
    # user = user_login =
    if user_age <= 18:
        return jsonify({"error": "your age must be at least 18"}), 400
    if (
        user_login.query.filter_by(user_email=user_email).first()
        or Admin_login.query.filter_by(admin_email=user_email).first
    ):
        return jsonify({"error": "Email already exist"}), 400
    HashedPassword = generate_password_hash(user_password)
    new_user_login = user_login(
        user_name=user_name,
        user_age=user_age,
        user_email=user_email,
        user_password=HashedPassword,
        user_pin = user_pin
    )

    try:
        db.session.add(new_user_login)
        db.session.commit()
        access_token = create_access_token(identity=user_email)
        refresh_token = create_refresh_token(identity=user_email)
        return (
            jsonify(
                {
                    "success": {
                        {"access_token": access_token},
                        {"refresh_token": refresh_token},
                    }
                }
            ),
            201,
        )
    except Exception:
        return jsonify({"error": Exception})

# * User login
@app.route("/user_login",methods=["POST"])
def user_login():
    data = request.get_json()
    if not data:
        return jsonify({"error":"Data must be in json format"}),400
    user_email = data.get("user_email")
    user_password = data.get("user_password")
    if not user_email or not user_password:
        return jsonify({"error":"all field are required"}),400
    user = user_login.query.filter_by(user_email=user_email).first
    if not user or not check_password_hash(user.user_password,user_password):
        return jsonify({"error":"email or password is in correct"}),401
    access_token=create_access_token(identity=user_email)
    refresh_token=create_refresh_token(identity=user_email)
    return (
            jsonify(
                {
                    "success": {
                        {"access_token": access_token},
                        {"refresh_token": refresh_token},
                    }
                }
            ),
            201,
        )

# * User Account
@app.route('/user_account',methods=["POST"])
def user_account():
    data = request.get_json()
    if not data:
        return ({"error":"Data must be in json format"})
    user_account_number = data.get("user_account_number") 
    user_account_pin = data.get("user_account_pin") 
    bank_balance = data.get("bank_balance") 

    bank_id = Bank.query.get(data["id"])
    user_id = user_id.query.get(data["id"])
# if not user_account_number or not user_account_pin or not bank_balance:


    if not user_account_number or not user_account_pin or not bank_balance:
        return jsonify({"error":"all field are required"}),401
    if bank_id is None:
        return jsonify({"error":"Bank does not exist"}),404

    if user_id is None:
        return jsonify({"error":"User does not exist"}),404

    new_user_account = user_login(user_account_number,user_account_pin,bank_balance)
    try:
        db.session.add(new_user_account)
        db.session.commit()
    except Exception:
        return jsonify({"error":Exception}),400
        
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5001)
