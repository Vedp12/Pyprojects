from flask import (
    Flask,
    request,
    jsonify,
    make_response,
    render_template,
    session,
    redirect,
    url_for,
)
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config["SECRET_KEY"] = "KlWRSoyb1CwI45SB0-wQYBD2FTBb_A"


# Decorator for protected routes
def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")  # Expect "Bearer <token>"
        if not token:
            return jsonify({"Alert": "Token is missing"}), 401
        try:
            token = token.split(" ")[1]
            payload = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"Alert": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"Alert": "Invalid Token"}), 401
        return func(*args, **kwargs)

    return decorated


# Public route
@app.route("/public")
def public():
    return "Accessible without login"


# Protected route
@app.route("/auths")
@token_required
def auth():
    return "JWT Verified - Secure Content"


# Home route
@app.route("/")
def home():
    if not session.get("logged_in"):
        return redirect(url_for("login_page"))
    return "You are logged in!"


# Login page (GET)
@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")


# Login form handler (POST)
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username and password == "1234":  # demo only
        session["logged_in"] = True
        token = jwt.encode(
            {
                "user": username,
                "exp": datetime.utcnow() + timedelta(minutes=2),
            },
            app.config["SECRET_KEY"],
            algorithm="HS256",
        )
        return jsonify({"token": token})
    else:
        return make_response(
            "Unable to verify",
            403,
            {"WWW-Authentication": 'Basic realm:"Authentication Failed!"'},
        )


# Logout route
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login_page"))


if __name__ == "__main__":
    app.run(debug=True)
