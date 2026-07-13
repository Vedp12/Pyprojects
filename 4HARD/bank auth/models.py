from flask_sqlalchemy import SQLAlchemy
from flask import url_for

db.sqlalchemy(app)
from sqlalchemy.exc import IntegrityError
import datetime

class Admin_login(db.Model):
    __tablename__ = "Admin_auths"
    id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String[160], nullable=False)
    admin_created = db.Column(db.datetime,default = datetime.utcnow)
    banks = db.relationship("")


class Bank(db.Model):
    __tablename__ = "banks"
    id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String[160], nullable=False)
    bank_address = db.Column(db.String[160], nullable=False)


class user_login(db.Model):
    __tablename__ = "user_auths"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String[160], nullable=False)
    user_age = db.Column(db.Integer, nullable=False)
    user_email = db.Column(db.String[40])


class user_account(db.Model):
    __tablename__ = "user_accounsts"
    id = db.Column(db.Integer, primary_key=True)
    user_account_name = db.Column(db.String[160], nullable=False)
    user_account_number = db.Column(db.Integer, nullable=True)
    user_account_pin = db.Column(db.Integer, nullable=True)


class user_deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Deposite_Value = db.Column(db.Integer)


class user_withdraw(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    withdrawal_Value = db.Column(db.Integer)
