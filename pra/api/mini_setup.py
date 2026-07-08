from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, create_refresh_token

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "data"
jwt=JWTManager(app)

user = {"tux": "abc123x",
        "ved":"123abc"}
@app.route('/login',methods=["POST"])
def login():
    username=request.json.get("username",None)
    password=request.json.get("password",None)
    
    if user.get(username) != password:
        return jsonify({"msg":"username or Password is incorrect!"}),401
    refresh_token = create_refresh_token(identity=username)
    return jsonify(refresh_token=refresh_token)

@app.route('/protected',methods=["GET"])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify({"token": current_user}), 200

if __name__ == "__main__":
    app.run(debug=True)
    
