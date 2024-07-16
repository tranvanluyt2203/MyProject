from flask import Flask, request, jsonify, g, redirect, url_for
import jwt
import datetime
from firebase_admin import credentials, auth, firestore, db
import firebase_admin
from firebase_admin import firestore
import json
from tqdm import tqdm
from utilies.Password import hash, CheckPasswordFormat

# Create an instance of the Flask class
app = Flask(__name__)
SECRET_KEY = "Bearer"

cred = credentials.Certificate(
    "./Firebase/myschedule-97187-firebase-adminsdk-306cs-00a5a22c4c.json"
)
firebase_admin.initialize_app(
    cred,
    {"databaseURL": "https://myschedule-97187-default-rtdb.firebaseio.com"},
)
db_firestore = firestore.client()

valid_tokens = set()


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


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
