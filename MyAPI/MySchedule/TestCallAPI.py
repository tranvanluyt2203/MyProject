import requests
from APIs.ListAPIURL import *


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
    print("Register")
    # email = input("Enter email: ")
    # password = input("Enter password: ")
    data = {"email": "tranvanluyt12b4@gmail.com", "password": "Travanluyt.2203"}
    try:
        # response = requests.post(url, json=data, headers=headers)
        response = requests.post(url, json=data)
        print("Response", response.json())
    except requests.RequestException as e:
        print("Request failed:", e)

def PrintSelect():
    print("Enter select")
    print("1.Register")
    print("2.Login")

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
            case 0:
                return
        PrintSelect()
        select = int(input("Type your select: "))


if __name__ == "__main__":
    main()
