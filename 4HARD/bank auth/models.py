from flask_sqlalchemy import SQLAlchemy
from flask import url_for

from sqlalchemy.exc import IntegrityError
from datetime import datetime, timezone
db = SQLAlchemy()

class Admin_login(db.Model):
    __tablename__ = "admin_login"
    id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(160), nullable=False)
    admin_email = db.Column(db.String(160), unique=True, nullable=False, index=True)
    admin_password = db.Column(db.String(150), nullable=False)
    admin_created = db.Column(
        db.DateTime, 
        default=lambda: datetime.now(timezone.utc)
    )
    banks = db.relationship("Bank", lazy=True, backref="Admin_login")


class Bank(db.Model):
    __tablename__ = "banks"
    id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(160), nullable=False)
    bank_address = db.Column(db.String(160), nullable=False)

    user_account = db.relationship("user_account", lazy=True, backref="Bank")
    admin_id = db.Column(db.Integer, db.ForeignKey("admin_login.id"), nullable=False)


class user_login(db.Model):
    __tablename__ = "user_login"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(160), nullable=False)
    user_age = db.Column(db.Integer, nullable=False)
    user_email = db.Column(db.String(40))
    user_password = db.Column(db.String(150), nullable=False)
    user_pin = db.Column(db.Integer,nullable=False)
    user_account = db.relationship("user_account",lazy=True,backref="user_login")
    user_created = db.Column(
        db.DateTime, 
        default=lambda: datetime.now(timezone.utc)
    )

class user_account(db.Model):
    __tablename__ = "user_accounts"
    id = db.Column(db.Integer, primary_key=True)
    user_account_number = db.Column(db.Integer, nullable=True)
    user_account_pin = db.Column(db.Integer, nullable=True)
    bank_balance = db.Column(db.Float)

    user_id = db.Column(db.Integer, db.ForeignKey("user_login.id",nullable=False))
    bank_id = db.Column(db.Integer, db.ForeignKey("bank.id"), nullable=False)


class user_deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Deposite_Value = db.Column(db.Float)


class user_withdraw(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    withdrawal_Value = db.Column(db.Float)
