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
        db.reference(DATABASE_USER_NAME).child(DATABASE_OPERATION_NAME).child(
            user.uid
        ).set({TIME_REGISTER: datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        accessToken = "shop" + user.uid + "app"
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
        db_firestore.collection(DATABASE_USER_NAME).document(user.uid).set(user_data)
        db_firestore.collection(DATABASE_PROFILE_USER_NAME).document(user.uid).set(
            profile
        )

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
            ref = db_firestore.collection(DATABASE_USER_NAME).document(user.uid).get()
            if ref.get("password") == hash(password):
                accessToken = ref.get("accessToken")
                valid_tokens.add(SECRET_KEY + accessToken)
                db.reference(DATABASE_USER_NAME).child(DATABASE_OPERATION_NAME).child(
                    user.uid
                ).update({TIME_LOGIN: datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
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
                        "error": "Email is not exists",
                    }
                ),
                401,
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
        profile = (
            db_firestore.collection(DATABASE_PROFILE_USER_NAME)
            .document(userId)
            .get()
            .to_dict()
        )
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
            db.reference(DATABASE_USER_NAME).child(DATABASE_OPERATION_NAME).child(
                userId
            ).update({TIME_UPDATE: datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            db_firestore.collection(DATABASE_PROFILE_USER_NAME).document(userId).update(
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
        db.reference(DATABASE_USER_NAME).child(DATABASE_OPERATION_NAME).child(
            get_userId_from_headers(headers)
        ).update({TIME_LOGOUT: datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
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
            db_firestore.collection(DATABASE_USER_NAME)
            .document(userId)
            .get()
            .to_dict()
            .get("password")
        )
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
            if not (CheckPasswordFormat(newPassword)):
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
                db.reference(DATABASE_USER_NAME).child(DATABASE_OPERATION_NAME).child(
                    get_userId_from_headers(headers)
                ).update(
                    {TIME_CHANGE_PASSWORD: datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
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
# -----------------------------------STORE------------------------------------------------
# -------------------------------------------------------------------------------------------
@app.route(REGISTER_NEW_STORE, methods=["POST"])
def registerNewStore():
    data = request.json
    try:
        username = data.get("username")
        password = data.get("password")
        if not (CheckPasswordFormat(password)):
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
        storeId = hash(username + "-" + password)
        if (
            db_firestore.collection(DATABASE_STORE_NAME)
            .document(storeId)
            .get()
            .to_dict()
        ):
            return (
                jsonify({"error": "Store is exists"}),
                400,
            )
        else:
            accessToken = "store" + storeId + "store"
            dataStore = {
                "accessToken": accessToken,
                "username": hash(username),
                "password": hash(password),
            }
            dataDefaultProfileStore = {
                "nameShop": "",
                "phoneNumber": "",
                "avatar": "",
                "address": "",
                "dayOpen": "",
                "listProduct": [],
                "rateShop": 0,
                "license": "",
                "introduction": "",
            }
            db.reference(DATABASE_STORE_NAME).child(DATABASE_OPERATION_NAME).child(
                storeId
            ).set({TIME_REGISTER: datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            db_firestore.collection(DATABASE_STORE_NAME).document(storeId).set(
                dataStore
            )
            db_firestore.collection(DATABASE_INFOR_STORE_NAME).document(storeId).set(
                dataDefaultProfileStore
            )
        return (
            jsonify(
                {
                    "success": True,
                    "status": 200,
                    "message": "Register New Store is success",
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


@app.route(LOGIN_STORE, methods=["POST"])
def loginStore():
    dataLogin = request.json
    try:
        username = dataLogin.get("username")
        password = dataLogin.get("password")
        if not (CheckPasswordFormat(password)):
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
        storeId = hash(username + "-" + password)
        ref = db_firestore.collection(DATABASE_STORE_NAME).document(storeId).get()
        if not (ref.to_dict()):
            return (
                jsonify(
                    {
                        "error": "Account is not exists",
                    },
                ),
                401,
            )
        else:
            if hash(password) != ref.to_dict().get("password"):
                return (
                    jsonify(
                        {
                            "error": "Password is wrong",
                        },
                    ),
                    400,
                )
            else:
                data = ref.to_dict()
                valid_tokens.add(SECRET_KEY + data.get("accessToken"))
                db.reference(DATABASE_STORE_NAME).child(DATABASE_OPERATION_NAME).child(
                    storeId
                ).update({TIME_LOGIN: datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
                return (
                    jsonify(
                        {
                            "success": True,
                            "status": 200,
                            "data": {
                                "accessToken": data.get("accessToken"),
                            },
                        },
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


@app.route(LOGOUT_STORE, methods=["POST"])
def logoutStore():
    headers = request.headers.get("Authorization")
    isNotLogin = checkLogin(headers)
    if isNotLogin:
        return isNotLogin
    try:
        db.reference(DATABASE_STORE_NAME).child(DATABASE_OPERATION_NAME).child(
            get_storeId_from_headers(headers)
        ).update({TIME_LOGOUT: datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        valid_tokens.discard(headers)
        return (
            jsonify(
                {
                    "success": True,
                    "status": 200,
                    "message": "Logout Store success",
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
# -----------------------------------PRODUCTS------------------------------------------------
# -------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------
# -----------------------------------PRODUCTS------------------------------------------------
# -------------------------------------------------------------------------------------------


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
