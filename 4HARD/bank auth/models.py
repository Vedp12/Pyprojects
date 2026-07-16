from flask_sqlalchemy import SQLAlchemy
from flask import url_for

from sqlalchemy.exc import IntegrityError
from datetime import datetime, timezone
db = SQLAlchemy()


class TokenBlocklist(db.Model):
    __tablename__ = "token_blocklist"
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))


class Admin_login(db.Model):
    __tablename__ = "admin_login"
    id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(160), nullable=False)
    admin_email = db.Column(db.String(160), unique=True, nullable=False, index=True)
    admin_password = db.Column(db.String(150), nullable=False)
    admin_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    banks = db.relationship("Bank", lazy=True, backref="admin")


class Bank(db.Model):
    __tablename__ = "banks"
    id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(160), nullable=False)
    bank_address = db.Column(db.String(160), nullable=False)
    user_account = db.relationship("user_account", lazy=True, backref="bank")
    bank_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    admin_id = db.Column(db.Integer, db.ForeignKey("admin_login.id"), nullable=False)


class User_login(db.Model):
    __tablename__ = "user_login"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(160), nullable=False)
    user_age = db.Column(db.Integer, nullable=False)
    user_email = db.Column(db.String(40))
    user_password = db.Column(db.String(150), nullable=False)
    user_account = db.relationship("user_account", lazy=True, backref="user")
    user_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

class User_account(db.Model):
    __tablename__ = "user_accounts"
    id = db.Column(db.Integer, primary_key=True)
    user_account_number = db.Column(db.Integer, nullable=True)
    user_pin = db.Column(db.Integer, nullable=False)

    bank_balance = db.Column(db.Float)
    userDeposit = db.relationship("user_deposit", lazy=True, backref="useraccount")
    userWithdraw = db.relationship("user_withdraw", lazy=True, backref="useraccount")

    user_id = db.Column(db.Integer, db.ForeignKey("user_login.id"), nullable=False)
    bank_id = db.Column(db.Integer, db.ForeignKey("banks.id"), nullable=False)


class User_deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Deposit_Value = db.Column(db.Float)
    pin = db.Column(db.Integer)

    Transaction_id=db.Column(db.string(120),nullable=False)
    Transaction_date=db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    user_account_id = db.Column(
        db.Integer, db.ForeignKey("user_accounts.id"), nullable=False
    )

class User_withdraw(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    withdrawal_Value = db.Column(db.Float)
    pin = db.Column(db.Integer)
    Transaction_id=db.Column(db.string(120),nullable=False)

    Transaction_date=db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    user_account_id = db.Column(
        db.Integer, db.ForeignKey("user_accounts.id"), nullable=False
    )
