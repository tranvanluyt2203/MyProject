import requests
from APIs.ListAPIURL import *

global accessToken
accessToken = ""
global SECRET_KEY
SECRET_KEY = "SHOP"


# ---------------------------------------USERS-----------------------------------------------


def register():
    url = BASE_API + REGISTER
    print("Register")
    # email = input("Enter email: ")
    # password = input("Enter password: ")
    # re_password = input("Re enter passsword: ")
    # while password != re_password:
    #     print("Password is not match!!!")
    #     password = input("Enter password: ")
    #     re_password = input("Re enter passsword: ")

    # data = {"email": email, "password": password}
    data = {"email": "tranvanluyt12b4@gmail.com", "password": "Tranvanluyt.2203"}
    try:
        # response = requests.post(url, json=data, headers=headers)
        response = requests.post(url, json=data)
        print("Response", response.json())
    except requests.RequestException as e:
        print("Request failed:", e)


def login():
    url = BASE_API + LOGIN
    print("Login")
    # email = input("Enter email: ")
    # password = input("Enter password: ")
    data = {
        "email": "tranvanluyt12b4@gmail.com",
        "password": "Tranvanluyt@2203",
    }  # Tranvanluyt@2203
    try:
        # response = requests.post(url, json=data, headers=headers)
        response = requests.post(url, json=data)
        print("Status code", response.status_code)
        print("Response", response.json())
        if response.status_code == 200:
            global accessToken
            accessToken = response.json().get("data").get("accessToken")
    except requests.RequestException as e:
        print("Request failed:", e)


def get_profile():
    url = BASE_API + GET_PROFILE
    print("Get Profile")
    headers = {"Authorization": SECRET_KEY + accessToken}
    try:
        response = requests.get(url, headers=headers)
        print("Status code", response.status_code)
        print("Response", response.json())
    except requests.RequestException as e:
        print("Request failed:", e)


def update_profile():
    url = BASE_API + UPDATE_PROFILE
    print("Update Profile")
    headers = {"Authorization": SECRET_KEY + accessToken}
    try:
        data = {
            "fullName": "Trần Văn Luýt",
            "birthday": "22/03/2002",
            "address": "Đà Nẵng, Việt Nam",
        }
        response = requests.post(url, headers=headers, json=data)
        print("Status code", response.status_code)
        print("Response", response.json())
    except requests.RequestException as e:
        print("Request failed:", e)


def change_password():
    url = BASE_API + CHANGE_PASSWORD
    headers = {"Authorization": SECRET_KEY + accessToken}
    try:
        data = {
            "oldPassword": "Tranvanluyt.2203",
            "newPassword": "Tranvanluyt@2203",
        }
        response = requests.post(url, headers=headers, json=data)
        print("Status code", response.status_code)
        print("Response", response.json())
    except requests.RequestException as e:
        print("Request failed:", e)


def logout():
    url = BASE_API + LOGOUT
    print("Logout")
    global accessToken
    headers = {"Authorization": SECRET_KEY + accessToken}
    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            accessToken = ""
        print("Status code", response.status_code)
        print("Response", response.json())
    except requests.RequestException as e:
        print("Request failed:", e)


# ---------------------------------------STORE--------------------------------------------------
def registerStore():
    url = BASE_API + REGISTER_NEW_STORE
    data = {
        "username": "helloShop",
        "password": "HelloShop@2203",
    }
    try:
        response = requests.post(url, json=data)
        print("Status code", response.status_code)
        print("Response", response.json())
    except requests.RequestException as e:
        print("Request failed:", e)


def loginStore():
    url = BASE_API + LOGIN_STORE
    data = {
        "username": "helloShop",
        "password": "HelloShop@2203",
    }
    try:
        response = requests.post(url, json=data)
        print("Status code", response.status_code)
        print("Response", response.json())
        if response.status_code == 200:
            global accessToken
            accessToken = response.json().get("data").get("accessToken")

    except requests.RequestException as e:
        print("Request failed:", e)


def logoutStore():
    url = BASE_API + LOGOUT_STORE
    print("Logout")
    global accessToken
    headers = {"Authorization": SECRET_KEY + accessToken}
    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            accessToken = ""
        print("Status code", response.status_code)
        print("Response", response.json())
    except requests.RequestException as e:
        print("Request failed:", e)


def change_password_Store():
    url = BASE_API + CHANGE_PASSWORD_STORE
    headers = {"Authorization": SECRET_KEY + accessToken}
    data = {
        "oldPassword": "HelloShop@2203",
        "newPassword": "HelloShop@2203",
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        print("Status code", response.status_code)
        print("Response", response.json())
    except requests.RequestException as e:
        print("Request failed:", e)


def get_profile_Store():
    url = BASE_API + INFOR_STORE
    headers = {"Authorization": SECRET_KEY + accessToken}
    try:
        response = requests.get(url, headers=headers)
        print("Status code", response.status_code)
        print("Response", response.json())
    except requests.RequestException as e:
        print("Request failed:", e)


def update_profile_Store():
    url = BASE_API + UPDATE_INFOR_STORE
    headers = {"Authorization": SECRET_KEY + accessToken}
    try:
        data = {
            "address": "Liên Chiểu - Đà Nẵng",
            "avatar": "https://img.freepik.com/free-vector/cartoon-style-cafe-front-shop-view_134830-697.jpg",
            "dayOpen": "21/07/2024",
            "introduction": "tittle hello this is shop abc bán quần áo \n hỗn hợp đầy đủ yêu cầu ",
            "license": "",
            "listProduct": [],
            "nameShop": "TestShop",
            "phoneNumber": "01223456789",
            "rateShop": 5,
        }
        response = requests.post(url, headers=headers, json=data)
        print("Status code", response.status_code)
        print("Response", response.json())
    except requests.RequestException as e:
        print("Request failed:", e)
    return


def add_product():
    return

def get_product():
    return

def delete_product():
    return


# ---------------------------------------PRODUCT-----------------------------------------------
def pushProduct():
    return


def getInforProduct():
    return


def updateInforProduct():
    return


# _______________________________________________________________________________________________


def SelectObject():
    print("Select Object:")
    print("1.User")
    print("2.Store")
    print("3.Product")
    select = int(input("Your Select: "))
    return select


def FunctionUser():
    print("Enter select function for user")
    print("1.Register")
    print("2.Login")
    print("3.Logout")
    print("4.Change Password")
    print("5.Get Profile")
    print("6.Update profile")

    print("0.To out")


def FunctionStore():
    print("Enter select function for store")
    print("1.Register")
    print("2.Login")
    print("3.Logout")
    print("4.Change Password")
    print("5.Get Infor Store")
    print("6.Update Infor Store")
    print("7.Add Product")
    print("8.Get Product")
    print("9.Delete Product")

    print("0.To out")


def FunctionProduct():
    print("Enter select function for product")
    print("1. Push product")
    print("2. Infor product")
    print("3. Update infor product")

    print("0.To out")


def SelectFunctionUser():
    FunctionUser()
    select = int(input("Type your select: "))
    while select != 0:
        match select:
            case 1:
                register()
            case 2:
                login()
            case 3:
                logout()
            case 4:
                change_password()
            case 5:
                get_profile()
            case 6:
                update_profile()
            case 0:
                return
        FunctionUser()
        select = int(input("Type your select: "))


def SelectFuntionStore():
    FunctionStore()
    select = int(input("Type your select: "))
    while select != 0:
        match select:
            case 1:
                registerStore()
            case 2:
                loginStore()
            case 3:
                logoutStore()
            case 4:
                change_password_Store()
            case 5:
                get_profile_Store()
            case 6:
                update_profile_Store()
            case 7:
                add_product()
            case 8:
                get_product()
            case 9:
                delete_product()
            case 0:
                return
        FunctionStore()
        select = int(input("Type your select: "))


def SelectFunctionProduct():
    while select != 0:
        match select:
            case 1:
                pushProduct()
            case 2:
                getInforProduct()
            case 3:
                updateInforProduct()
            case 0:
                return
        FunctionProduct()
        select = int(input("Type your select: "))


def main():
    yes = "y"
    while yes == "y":
        select_ = SelectObject()
        if select_ == 1:
            SelectFunctionUser()
        if select_ == 2:
            SelectFuntionStore()
        if select_ == 3:
            SelectFunctionProduct()
        yes = input("Do you want test ? (y-yes or skip to exit) : ")


if __name__ == "__main__":
    main()
