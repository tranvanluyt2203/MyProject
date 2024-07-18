from flask import Flask, request, jsonify, g, redirect, url_for
import jwt
import datetime
from firebase_admin import credentials, auth, firestore, db
import firebase_admin
from firebase_admin import firestore
import json
from tqdm import tqdm

from utilies.Password import hash, CheckPasswordFormat
from utilies.Email import CheckEmailFormat
from APIs.SettingAPI import *
from APIs.ListAPIURL import *


# Create an instance of the Flask class
app = Flask(__name__)


def checkAccountInfor(email, password):
    if not (CheckEmailFormat(email)):
        return (
            jsonify(
                {
                    "success": False,
                    "status": 400,
                    "message": "Email is not format",
                }
            ),
            400,
        )
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


@app.route(REGISTER, methods=["POST"])
def register():
    email = request.json.get("email")
    password = request.json.get("password")
    if checkAccountInfor(email, password):
        return checkAccountInfor(email, password)
    try:
        user = auth.create_user(email=email, password=password)
        accessToken = "schedule" + user.uid + "app"
        user_data = {
            "accessToken": accessToken,
            "email": email,
            "password": hash(password),
        }
        profile = {
            "fullName": "",
            "email": email,
            "birth_day": "",
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
    if checkAccountInfor(email, password):
        return checkAccountInfor(email, password)
    try:
        user = auth.get_user_by_email(email)
        if user:
            ref = db_firestore.collection("users").document(user.uid).get()
            if ref.get("password") == hash(password):
                accessToken = ref.get("accessToken")
                valid_tokens.add(SECRET_KEY + accessToken)
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


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
