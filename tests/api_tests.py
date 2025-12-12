import requests

# Check successful response
def successful_response():
    url = "https://reqres.in/api/users/1"
    res = requests.get(url)

    assert res.status_code == 200


# Check response content
def response_content():
    url = "https://reqres.in/api/users/1"
    res = requests.get(url)

    data = res.json()  
    assert "data" in data
    assert data["data"]["id"] == 1

 
#  test single user details
def single_user():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 2
    assert "first_name" in data["data"]
    assert "last_name" in data["data"]

# User not found test
def user_not_found():
    response = requests.get("https://reqres.in/api/users/99999")

    assert response.status_code == 404

    # delete user test
def test_delete_user():
    """Test deleting a user"""
    response = requests.delete("https://reqres.in/api/users/2")
    assert response.status_code == 204

# Check for missing password error
def password_error():
    url = "https://reqres.in/api/register"
    payload = {"email": "mdshoeb1011@gmail..com"}

    res = requests.post(url, json=payload)
    assert res.status_code == 400

    data = res.json()
    assert data["error"] == "Missing password"

# invalid email login test
def invalid_email():
    login_data = {"email": "invalid", "password": "test"}
    response = requests.post("https://reqres.in/api/login", json=login_data)
    assert response.status_code == 400

    # TO Run     pytest api_tests.py -v