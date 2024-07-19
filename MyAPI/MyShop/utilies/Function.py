from flask import jsonify

from utilies.Email import *
from utilies.Password import *
from APIs.SettingAPI import SECRET_KEY, valid_tokens


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


def checkLogin(headers):
    if headers == SECRET_KEY:
        return (
            jsonify(
                {
                    "error": "No login",
                },
            ),
            401,
        )
    elif not (headers in valid_tokens):
        return (
            jsonify(
                {
                    "error": "Token is not valid",
                },
            ),
            401,
        )


def get_userId_from_headers(headers):
    return headers.split(SECRET_KEY)[1].split("SHOP")[1].split("app")[0]
