import requests

def login_user(email, password, repo_url):
    url = f"{repo_url}/login"
    payload = {"email": email, "password": password}
    response = requests.post(url, json=payload)
    print("login response")
    print(response.json())
    if response.status_code == 200:
        print("Login Successful!")
        return response.json()["access_token"]
    else:
        print(f"Failed to log in! Status Code: {response.status_code}, Response: {response.text}")
        return None