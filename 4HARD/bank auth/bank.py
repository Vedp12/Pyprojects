from flask import Flask,jsonify,request,redirect
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token,create_refresh_token,jwt_required,
    get_jwt,get_jwt_identity
)
from sqlalchemy.exc import IntegrityError
import os 
from environs import Env
from datetime import timedelta

env = Env()
env.read_env()
app = Flask(__app__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLAlchemy_DATABASE_URI"] = (f"sqlite:///{os.path.join(basedir,'bank.db')}" )

app.config["SQLAlchemy_TRACK_MODIFICATIONS"] = True

try:
    app.config["JWT_SECRET_KEY"] = env.str("JWT_STR_KEY")
except Exception:
    app.config["JWT_SECRET_KEY"] = "5Y4E3rlhAWL83q883ru5DwVUYpjglBU4FsJAMFWEqLs1e52ZJZuxrB3d64uYKbC77IttdMXv6KxdtnrMSw000cNdKkJWZCNxxaxV3WSIUcIEFFuxjeMKbKGjTwtWkF4F8stEF8QspWsyb5bCSsPZQPwPG"

finally:
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=20)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)


    # TODO: Add total bank and total address to bankends in admin panel
    # TODO: Add total total users bank panel
    # TODO: Add many to many relationship between bank and an admin 
    # TODO: Add one to many relationship between bank and user