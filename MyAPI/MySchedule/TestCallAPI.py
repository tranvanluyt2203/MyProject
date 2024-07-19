import requests
from APIs.ListAPIURL import *

global accessToken
accessToken = ""
global SECRET_KEY
SECRET_KEY = "SCHEDULE"


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
    data = {"email": "tranvanluyt12b4@gmail.com", "password": "Travanluyt.2203"}
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
    data = {"email": "tranvanluyt12b4@gmail.com", "password": "Tranvanluyt.2203"}
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
            "oldPassword": "Travanluyt.2203",
            "newPassword": "Tranvanluyt.2203",
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


def PrintSelect():
    print("Enter select")
    print("1.Register")
    print("2.Login")
    print("3.Get Profile")
    print("4.Update profile")
    print("5.Change Password")
    print("10.Logout")

    print("0.To out")


def main():
    PrintSelect()
    select = int(input("Type your select: "))
    while select != 0:
        match select:
            case 1:
                register()
            case 2:
                login()
            case 3:
                get_profile()
            case 4:
                update_profile()
            case 5:
                change_password()
            case 10:
                logout()
            case 0:
                return
        PrintSelect()
        select = int(input("Type your select: "))


if __name__ == "__main__":
    main()
