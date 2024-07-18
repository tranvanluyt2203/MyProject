from firebase_admin import credentials, auth, firestore, db

from firebase_admin import firestore
import firebase_admin

DOMAIN = "http://127.0.0.1:5000"

SECRET_KEY = "SCHEDULE"

cred = credentials.Certificate(
    "./Firebase/myschedule-97187-firebase-adminsdk-306cs-00a5a22c4c.json"
)
firebase_admin.initialize_app(
    cred,
    {"databaseURL": "https://myschedule-97187-default-rtdb.firebaseio.com"},
)
db_firestore = firestore.client()

valid_tokens = set()