from APIs.SettingAPI import DOMAIN, API_USER, API_PRODUCT, API_STORE,API_CART

BASE_API = DOMAIN

HOME_API = "/"
# -----------------------------------USERS---------------------------------------------------

REGISTER = API_USER + "register"
LOGIN = API_USER + "login"
LOGOUT = API_USER + "logout"
GET_PROFILE = API_USER + "getProfile"
UPDATE_PROFILE = API_USER + "updateProfile"
CHANGE_PASSWORD = API_USER + "changePassword"

# -----------------------------------PRODUCTS---------------------------------------------------
PUSH_PRODUCT = API_PRODUCT + "pushProduct"
INFOR_PRODUCT = API_PRODUCT + "getInforProduct"
UPDATE_INFOR_PRODUCT = API_PRODUCT + "updateInforProduct"
SEARCH_PRODUCT_BY_NAME = API_PRODUCT + "searchProductByName"

# -----------------------------------CART---------------------------------------------------
GET_CART = API_CART + "getCart"
ADD_PRODUCT_TO_CART = API_CART + "addToCart"

# -----------------------------------STORES---------------------------------------------------
REGISTER_NEW_STORE = API_STORE + "registerNewStore"
LOGIN_STORE = API_STORE + "loginStore"
INFOR_STORE = API_STORE + "getInforStore"
UPDATE_INFOR_STORE = API_STORE + "updateInforStore"
GET_PRODUCTS_STORE = API_STORE + "getProductsStore"
ADD_PRODUCT_TO_STORE = API_STORE + "addProductsStore"
DELETE_PRODUCT = API_STORE + "deleteProduct"
CHANGE_PASSWORD_STORE = API_STORE + "changePasswordStore"
LOGOUT_STORE = API_STORE + "logoutStore"
GET_LIST_STORE = API_STORE + "getListStore"


