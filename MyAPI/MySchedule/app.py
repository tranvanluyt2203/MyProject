from flask import Flask, request, jsonify, g, redirect, url_for
import jwt
import datetime
from firebase_admin import credentials, auth, firestore, db
import firebase_admin
from firebase_admin import firestore
import json
from tqdm import tqdm
from datetime import datetime

from utilies.Password import hash, CheckPasswordFormat
from utilies.Email import CheckEmailFormat
from utilies.Function import *
from APIs.SettingAPI import *
from APIs.ListAPIURL import *


app = Flask(__name__)


# -------------------------------------------------------------------------------------------


@app.route("/", methods=["GET"])
def home():
    return (
        jsonify(
            {
                "status": "Success",
                "message": "THIS IS HOME API",
            }
        ),
        201,
    )

# -------------------------------------------------------------------------------------------
# -----------------------------------USERS---------------------------------------------------
# -------------------------------------------------------------------------------------------

@app.route(REGISTER, methods=["POST"])
def register():
    email = request.json.get("email")
    password = request.json.get("password")
    isValidAccount = checkAccountInfor(email, password)
    if isValidAccount:
        return isValidAccount
    try:

        user = auth.create_user(email=email, password=password)
        db.reference("operationTime").child(user.uid).set(
            {"timeRegister": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        )
        accessToken = "schedule" + user.uid + "app"
        user_data = {
            "accessToken": accessToken,
            "email": email,
            "password": hash(password),
        }
        profile = {
            "fullName": "",
            "email": email,
            "birthday": "",
            "avatar": "https://ss-images.saostar.vn/wp700/pc/1613810558698/Facebook-Avatar_3.png",
        }
        db_firestore.collection("users").document(user.uid).set(user_data)
        db_firestore.collection("profiles").document(user.uid).set(profile)

        return (
            jsonify(
                {
                    "success": True,
                    "status": 201,
                    "message": "User register successfully",
                    "data": {
                        "accessToken": accessToken,
                    },
                }
            ),
            201,
        )
    except firebase_admin.auth.EmailAlreadyExistsError:
        return (
            jsonify(
                {
                    "error": "Email already exists",
                }
            ),
            400,
        )
    except Exception as e:
        return (
            jsonify(
                {
                    "error": str(e),
                }
            ),
            500,
        )


@app.route(LOGIN, methods=["POST"])
def login():
    email = request.json.get("email")
    password = request.json.get("password")
    isValidAccount = checkAccountInfor(email, password)
    if isValidAccount:
        return isValidAccount
    try:
        user = auth.get_user_by_email(email)
        if user:
            ref = db_firestore.collection("users").document(user.uid).get()
            if ref.get("password") == hash(password):
                accessToken = ref.get("accessToken")
                valid_tokens.add(SECRET_KEY + accessToken)
                db.reference("operationTime").child(user.uid).update(
                    {"timeLogin": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                )
                return (
                    jsonify(
                        {
                            "success": True,
                            "status": 200,
                            "message": "Login success",
                            "data": {
                                "accessToken": accessToken,
                            },
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "error": "Invalid password",
                        }
                    ),
                    401,
                )
        else:
            return (
                jsonify(
                    {
                        "error": "error",
                    }
                ),
                400,
            )
    except Exception as e:
        return (
            jsonify(
                {"error": str(e)},
            ),
            400,
        )


@app.route(GET_PROFILE, methods=["GET"])
def getProfile():
    headers = request.headers.get("Authorization")
    isNotLogin = checkLogin(headers)
    if isNotLogin:
        return isNotLogin
    try:
        userId = get_userId_from_headers(headers)
        profile = db_firestore.collection("profiles").document(userId).get().to_dict()
        return (
            jsonify(
                {
                    "success": True,
                    "status": 200,
                    "message": "Get profile success",
                    "data": {
                        "profile": profile,
                    },
                },
            ),
            201,
        )
    except Exception as e:
        return (
            jsonify(
                {"error": str(e)},
            ),
            400,
        )


@app.route(UPDATE_PROFILE, methods=["POST"])
def updateProfile():
    headers = request.headers.get("Authorization")
    isNotLogin = checkLogin(headers)
    if isNotLogin:
        return isNotLogin
    try:
        dataUpdateProfile = request.json
        if dataUpdateProfile:
            userId = get_userId_from_headers(headers)
            db.reference("operationTime").child(userId).update(
                {"timeUpdateProfile": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            )
            db_firestore.collection("profiles").document(userId).update(
                dataUpdateProfile
            )
            return (
                jsonify(
                    {
                        "success": True,
                        "status": 200,
                        "message": "Update profile success",
                    },
                ),
                200,
            )
        else:
            return (
                jsonify({"error": "No data profile to update"}),
                400,
            )

    except Exception as e:
        return (
            jsonify(
                {"error": str(e)},
            ),
            400,
        )


@app.route(LOGOUT, methods=["POST"])
def logout():
    headers = request.headers.get("Authorization")
    isNotLogin = checkLogin(headers)
    if isNotLogin:
        return isNotLogin
    try:
        db.reference("operationTime").child(get_userId_from_headers(headers)).update(
            {"timeLogout": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        )
        valid_tokens.discard(headers)
        return (
            jsonify(
                {
                    "success": True,
                    "status": 200,
                    "message": "Logout success",
                }
            ),
            200,
        )

    except Exception as e:
        return (
            jsonify(
                {"error": str(e)},
            ),
            400,
        )


@app.route(CHANGE_PASSWORD, methods=["POST"])
def changePassword():
    headers = request.headers.get("Authorization")
    isNotLogin = checkLogin(headers)
    if isNotLogin:
        return isNotLogin
    try:
        oldPasswordEnter = request.json.get("oldPassword")
        if not (CheckPasswordFormat(oldPasswordEnter)):
            return (
                jsonify(
                    {
                        "success": False,
                        "status": 400,
                        "message": "Password is not format",
                    }
                ),
                400,
            )
        userId = get_userId_from_headers(headers)
        oldpassword = (
            db_firestore.collection("users")
            .document(userId)
            .get()
            .to_dict()
            .get("password")
        )
        print(oldpassword)
        print(hash(oldPasswordEnter))
        if hash(oldPasswordEnter) != oldpassword:
            return (
                jsonify(
                    {
                        "success": False,
                        "status": 400,
                        "message": "Old Password is wrong",
                    }
                ),
                400,
            )
        else:
            newPassword = request.json.get("newPassword")
            if not(CheckPasswordFormat(newPassword)):
                return (
                    jsonify(
                        {
                            "success": False,
                            "status": 400,
                            "message": "New Password is not format",
                        }
                    ),
                    400,
                )
            else:
                db.reference("operationTime").child(
                    get_userId_from_headers(headers)
                ).update(
                    {"timeChangePassword": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                )
                db_firestore.collection("users").document(userId).update(
                    {"password": hash(newPassword)}
                )
                return (
                    jsonify(
                        {
                            "success": True,
                            "status": 200,
                            "message": "Change Password success",
                        }
                    ),
                    200,
                )

    except Exception as e:
        return (
            jsonify(
                {"error": str(e)},
            ),
            400,
        )
# -------------------------------------------------------------------------------------------
# -----------------------------------EVENTS--------------------------------------------------
# -------------------------------------------------------------------------------------------

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
