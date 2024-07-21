from firebase_admin import credentials, auth, firestore, db

from firebase_admin import firestore
import firebase_admin

DOMAIN = "http://127.0.0.1:5000"

API_USER = "/api/v1/users/"

API_CART = "api/v1/cart/"

API_PRODUCT = "/api/v1/products/"

API_STORE = "/api/v1/stores/"

SECRET_KEY = "SHOP"
# ----------------------------------NAME DATABASE---------------------------------------
DATABASE_USER_NAME = "users"
DATABASE_STORE_NAME = "stores"

# ----------------------FIRESTORE------------------------
DATABASE_PROFILE_USER_NAME = "profiles"

DATABASE_INFOR_STORE_NAME = "profilesStore"

DATABASE_CART_NAME = "carts"

DATABASE_PRODUCT_NAME = "products"

DATABASE_CATEGORIES_NAME = "categories"


# ----------------------REALTIME------------------------

DATABASE_OPERATION_NAME = "operationTime"
# ------------------------------------------------NAME VARIABLE OPERATION---------------------------------------
TIME_REGISTER = "timeRegister"
TIME_LOGIN = "timeLogin"
TIME_LOGOUT = "timeLogout"
TIME_UPDATE = "timeUpdateInfor"
TIME_CHANGE_PASSWORD = "timeChangepassword"
TIME_ADD_PRODUCT_TO_STORE = "timeAddProductStore"
TIME_ADD_PRODUCT_TO_CART = "timeAddProductCart"
TIME_APPEAR_PRODUCT = "timeAppearProduct"


#===============================================================================================================
cred = credentials.Certificate(
    "Firebase/myshop-54fbc-firebase-adminsdk-ysf7c-539c6b218d.json"
)
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://myshop-54fbc-default-rtdb.asia-southeast1.firebasedatabase.app"
    },
)
db_firestore = firestore.client()

valid_tokens = set()
