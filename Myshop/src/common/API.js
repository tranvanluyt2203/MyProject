let Domain = require("../common/Domain")
export const BASE_API = Domain.API_SERVER;
export const DOMAIN_API = BASE_API + '/';

export const API_USER = DOMAIN_API + Domain.API_USER
export const API_PRODUCT = DOMAIN_API + Domain.API_PRODUCT
export const API_STORE = DOMAIN_API + Domain.API_STORE
export const API_CART = DOMAIN_API + Domain.API_CART


// # -----------------------------------USERS---------------------------------------------------

export const REGISTER = API_USER + "register"
export const LOGIN = API_USER + "login"
export const LOGOUT = API_USER + "logout"
export const GET_PROFILE = API_USER + "getProfile"
export const UPDATE_PROFILE = API_USER + "updateProfile"
export const CHANGE_PASSWORD = API_USER + "changePassword"

// # -----------------------------------PRODUCTS---------------------------------------------------
export const PUSH_PRODUCT = API_PRODUCT + "pushProduct"
export const INFOR_PRODUCT = API_PRODUCT + "getInforProduct"
export const UPDATE_INFOR_PRODUCT = API_PRODUCT + "updateInforProduct"
export const SEARCH_PRODUCT_BY_NAME = API_PRODUCT + "searchProductByName"

// # -----------------------------------CART---------------------------------------------------
export const GET_CART = API_CART + "getCart"
export const ADD_PRODUCT_TO_CART = API_CART + "addToCart"

// # -----------------------------------STORES---------------------------------------------------
export const REGISTER_NEW_STORE = API_STORE + "registerNewStore"
export const LOGIN_STORE = API_STORE + "loginStore"
export const INFOR_STORE = API_STORE + "getInforStore"
export const UPDATE_INFOR_STORE = API_STORE + "updateInforStore"
export const GET_PRODUCTS_STORE = API_STORE + "getProductsStore"
export const ADD_PRODUCT_TO_STORE = API_STORE + "addProductsStore"
export const DELETE_PRODUCT = API_STORE + "deleteProduct"
export const CHANGE_PASSWORD_STORE = API_STORE + "changePasswordStore"
export const LOGOUT_STORE = API_STORE + "logoutStore"
export const GET_LIST_STORE = API_STORE + "getListStore"