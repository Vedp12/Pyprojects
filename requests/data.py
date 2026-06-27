
#! Login code
import requests

API_URL = "https://api.freeapi.app/api/v1/users/register"

payload = {
    "email": "ved68986@gmail.com",
    "password": "test@123",
    "role": "ADMIN",
    "username": "vedjohn"
}

def register():
    response = requests.post(API_URL, json=payload)

    data = response.json()

    if data["success"]:

        user = data["data"]["user"]

        print("Registration Successful")
        print("Username:", user["username"])
        print("Email:", user["email"])
        print("Role:", user["role"])

        print("\nMessage:")
        print(data["message"])

    else:
        print("Registration Failed")
        print(data["message"])


if __name__ == "__main__":
    register()

import requests

API_URL = "https://api.freeapi.app/api/v1/users/login"

payload = {
    "email": "ved68986@gmail.com",
    "password": "test@123",
}

#! Register code  
def login():
    try:
        response = requests.post(
            API_URL,
            json=payload,
            timeout=20
        )

        print(f"Status Code: {response.status_code}")

        # Raise exception for bad status codes
        response.raise_for_status()

        # Convert response to JSON
        data = response.json()

        # Check API success
        if data.get("success"):

            user = data["data"]["user"]

            print("\nLogin Successful")
            print("-" * 40)

            print("Username:", user.get("username"))
            print("Email:", user.get("email"))
            print("Role:", user.get("role"))

            print("\nAccess Token:")
            print(data["data"].get("accessToken"))

            print("\nRefresh Token:")
            print(data["data"].get("refreshToken"))

        else:
            print("Login Failed")
            print("Message:", data.get("message"))

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.ConnectionError:
        print("Connection error")

    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)

        try:
            print("Response:", response.json())
        except Exception:
            print("Raw Response:", response.text)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

    except ValueError:
        print("Invalid JSON response")

    except KeyError as e:
        print("Missing expected field:", e)


if __name__ == "__main__":
    login()
    