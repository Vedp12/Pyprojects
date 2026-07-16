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
from datetime import timedelta, datetime
from models import *
from functools import wraps
from uuid import uuid4
env = Env()
env.read_env()
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLAlCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir,'bank.db')}"
app.config["SQLAlCHEMY_TRACK_MODIFICATIONS"] = False

try:
    app.config["JWT_SECRET_KEY"] = env.str("JWT_STR_KEY")
except Exception:
    app.config["JWT_SECRET_KEY"] = (
        "5Y4E3rlhAWL83q883ru5DwVUYpjglBU4FsJAMFWEqLs1e52ZJZuxrB3d64uYKbC77IttdMXv6KxdtnrMSw000cNdKkJWZCNxxaxV3WSIUcIEFFuxjeMKbKGjTwtWkF4F8stEF8QspWsyb5bCSsPZQPwPG"
    )

finally:
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=20)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

db.init_app(app)
jwt = JWTManager(app)

# * Refresh
@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify({"access_token": new_access_token}), 200


# * Logout all
# ! It runs on every logged in request
@jwt.token_in_blocklist_loader
def check_if_revoked(jwt_header,jwt_payload):
    jti = jwt_payload["jti"]
    return db.session.query(TokenBlocklist.id).filter_by(jti=jti).first() is not None

# ! logout route
@app.route("/logout",methods=["DELETE"])
@jwt_required
def logout():
    jti = get_jwt("jti")
    db.session.add(TokenBlocklist(jti=jti))
    return jsonify({"msg":"logout successfuyy"}),200

# *Admin required decorator
def admin_required():
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()  # Ensures a valid JWT is present first
        def decorator(*args, **kwargs):
            claims = get_jwt()
            # Check if the custom claim 'is_admin' exists and is True
            if claims.get("is_admin") is True:
                return fn(*args, **kwargs)
            else:
                return jsonify({"msg": "Administration access required."}), 403
        return decorator
    return wrapper

# *Admin
# ? Signup
@app.route("/admin_signup", methods=["POST"])
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
    if not any(domain in admin_email for domain in email_list) in admin_email:
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
        refresh_token: object = create_refresh_token(identity=admin_email)
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

    user = Admin_login.query.filter_by(admin_email=admin_email).first()
    email_list = ["@gmail", "@yahoo", "@tuka", "@outlook"]
    if not any(domain in admin_email for domain in email_list) in admin_email:
        return f"email format is wrong use only: {[email_lists for email_lists in email_list]}"
    
    if not user or not check_password_hash(user.admin_password, admin_password):
        return jsonify({"error" "email or password is incorrect"}), 401
    access_token = create_access_token(identity=admin_email)
    refresh_token = create_refresh_token(identity=admin_email)
    return (
        jsonify({"access_token": access_token, "refresh_token": refresh_token}),201,
    )


# * Bank post
@app.route("/bank", methods=["POST"])
@admin_required()
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
    bank_id = Bank.query.get(data["id"])
    user_pin = data.get("user_pin")

    if bank_id is None:
        return jsonify({"error": "Bank id does not exist"}), 404

    if not user_name or not user_age or not user_email or not user_password or not user_pin:
        return jsonify({"error": "All field are required"}), 400
    # user = user_login =
    if user_age < 18:
        return jsonify({"error": "your age must be at least 18"}), 400
    email_list = ["@gmail", "@yahoo", "@tuka", "@outlook"]
    if not any(domain in user_email for domain in email_list) in user_email:
        return f"email format is wrong use only: {[email_lists for email_lists in email_list]}"
    
    if (
        User_login.query.filter_by(user_email=user_email).first()
        or Admin_login.query.filter_by(admin_email=user_email).first
    ):
        return jsonify({"error": "Email already exist"}), 400
    HashedPassword = generate_password_hash(user_password)
    new_user_login = User_login(
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
@app.route("/userlogin",methods=["POST"])
def userlogin():
    data = request.get_json()
    if not data:
        return jsonify({"error":"Data must be in json format"}),400
    user_email = data.get("user_email")
    user_password = data.get("user_password")
    if not user_email or not user_password:
        return jsonify({"error":"all field are required"}),400
    email_list = ["@gmail", "@yahoo", "@tuka", "@outlook"]
    if not any(domain in user_email for domain in email_list) in user_email:
        return f"email format is wrong use only: {[email_lists for email_lists in email_list]}"
    
    user = User_login.query.filter_by(user_email=user_email).first()
    
    if not user or not check_password_hash(user.user_password,user_password):
        return jsonify({"error":"email or password is in correct"}),401
    
    access_token=create_access_token(identity=user_email)
    refresh_token=create_refresh_token(identity=user_email)
    return (
            jsonify(
                {
                    "success": {
                        {"access_token": access_token},
                        {"refresh_token": refresh_token}
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
        return jsonify({"error":"Data must be in json format"}),400
    user_account_number = data.get("user_account_number")
    user_pin = data.get("user_pin")

    bank_balance = data.get("bank_balance") 

    bank_id = Bank.query.get(data["id"])
    user_id = User_login.query.get(data["id"])


    if not user_account_number or not bank_balance or not user_pin:
        return jsonify({"error":"all field are required"}),401
    if bank_id is None:
        return jsonify({"error":"Bank does not exist"}),404

    if user_id is None:
        return jsonify({"error":"User does not exist"}),404

    new_user_account = User_account(user_account_number,user_pin,bank_balance)
    try:
        db.session.add(new_user_account)
        db.session.commit()
    except Exception:
        return jsonify({"error":Exception}),400


@app.route("userDeposit",methods = ["POST"])
@jwt_required
def userDeposit():
    data = request.get_json()
    if not data:
        return jsonify({"error":"data is not in json format"}),401
    Deposit_Value = data.get("Deposit_Value")
    pin = data.get("pin")
    Transaction_id = data.get("Transaction_id")
    userAccount = user_account.query.get(data("id"))
    account_pin= User_account.query.get(data("user_pin"))
    if userAccount is None:
        return jsonify({"error": "User id does not exist"}), 404
    if account_pin != pin:
        return jsonify({"error": "Pin is not same"}), 401
    if not Deposit_Value or not pin or not Transaction_id:
        return jsonify({"error": "All field are required"}), 400
    UserBalance = user_account.query.get(data("bank_balance"))
    UserBalance += int(Deposit_Value)
    try:
        Transaction_id = f"{datetime.today().strftime('%Y-%m:%d')}-{uuid4()}"
        deposited = User_deposit(Deposit_Value, pin, Transaction_id)
        db.session.add(deposited)
        db.session.commit()
        return jsonify({"success":f"{Deposit_Value} added to bank account with transaction id {Transaction_id}"})
    except Exception:
        return  jsonify({"error":Exception}),400

@app.route('/userWithdrawal', methods=["POST"])
def userWithdrawal():
    data = request.get_json()
    if not data:
        return jsonify({"error":"Data must be in json format"}),400
    withdrawal_Value = data.get("withdrawal_Value")
    pin =data.get("pin")
    Transaction_id = data.get("Transaction_id")
    userAccount = user_account.query.get(data("id"))
    if userAccount is None:
        return jsonify({"error":"User id does not exist"}), 404
    UserBalance = user_account.query.get(data("bank_balance"))
    account_pin= User_account.query.get(data("user_pin"))
    if account_pin != pin:
        return jsonify({"error": "Pin is not same"}), 401
    if withdrawal_Value > UserBalance:
        return jsonify({"error": "Withdrawal value cannot be greater than balance. Try Putting less value"}), 400
    UserBalance -= int(withdrawal_Value)
    try:
        Transaction_id = f"{datetime.today().strftime('%Y-%m:%d')}-{uuid4()}"
        withdraw = User_withdraw(withdrawal_Value, pin, Transaction_id)
        db.session.add(withdraw)
        db.session.commit()
    except Exception:
        return jsonify({"error":Exception}),400

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5001)
