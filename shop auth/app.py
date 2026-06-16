"""
Street Bazaar - Shop Auth
Flask mini-project: signup / login with hashed passwords
"""

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# ── App & DB setup ──────────────────────────────────────────────────────────
app = Flask(__name__)
app.config["SECRET_KEY"]         = "change-this-in-production"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#TODO ── Model ───────────────────────────────────────────────────────────────────
class User(db.Model):
    """Shop owner account — password stored as bcrypt hash, never plaintext."""
    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(120), nullable=False)
    email    = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)   # hashed only

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

#TODO ── REST API ─────────────────────────────────────────────────────────────────
#! jsonify a utility function that converts Python dictionaries or objects into JSON-formatted HTTP responses.
#* POST /api/signup
@app.route("/api/signup", methods=["POST"])
def api_signup():
#!  silent=True is a parameter that suppresses errors and returns None instead of raising an exception when a requested resource or operation fails
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    name     = (data.get("name")     or "").strip()
    email    = (data.get("email")    or "").strip().lower()
    password = (data.get("password") or "").strip()

    #^ Prevent causes
    if not name or not email or not password:
        return jsonify({"error": "All fields are required"}), 400
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 409

    #^ Hash password before storing — never save plaintext
    hashed = generate_password_hash(password)
    user   = User(name=name, email=email, password=hashed)

    #^ Store data to DB
    db.session.add(user)
    db.session.commit()

    session["user_id"] = user.id
    session["user_name"] = user.name
    return jsonify({"message": "Account created", "user": user.to_dict()}), 201

#* POST /api/login
@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "JSON body required"}), 400

    email    = (data.get("email")    or "").strip().lower()
    password = (data.get("password") or "").strip()

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()

    # Use check_password_hash — constant-time comparison, no timing attacks
    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid email or password"}), 401

    session["user_id"]   = user.id
    session["user_name"] = user.name
    return jsonify({"message": "Login successful", "user": user.to_dict()}), 200


@app.route("/api/logout", methods=["POST"])
def api_logout():
    session.clear()
    return jsonify({"message": "Logged out"}), 200

#TODO ── Page routes ──────────────────────────────────────────────────────────────
@app.route("/")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("home.html", name=session.get("user_name"))

@app.route("/signup")
def signup():
    if "user_id" in session:
        return redirect(url_for("home"))
    return render_template("signup.html")

@app.route("/login")
def login():
    if "user_id" in session:
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    with app.app_context():
        db.create_all()   # create tables on first run
    app.run(debug=True)
