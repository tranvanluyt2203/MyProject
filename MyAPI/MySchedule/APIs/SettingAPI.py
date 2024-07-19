from firebase_admin import credentials, auth, firestore, db

from firebase_admin import firestore
import firebase_admin

DOMAIN = "http://127.0.0.1:5000"

API_USER = "/api/v1/users/"

SECRET_KEY = "SCHEDULE"

cred = credentials.Certificate(
    "Firebase/myshop-54fbc-firebase-adminsdk-ysf7c-539c6b218d.json"
)
firebase_admin.initialize_app(
    cred,
    {"databaseURL": "https://myshop-54fbc-default-rtdb.asia-southeast1.firebasedatabase.app"},
)
db_firestore = firestore.client()

valid_tokens = set()
