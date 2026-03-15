import json
import jsonpath
import requests
import pytest

@pytest.fixture
def user_id():
    url = "https://69b675b7583f543fbd9dc80a.mockapi.io/testproject/users"

    f = open("C:\\Users\\Felhasználó\\Documents\GitHub\\API testing\\user.json", "r")
    request_stream = f.read()
    request_json = json.loads(request_stream)
    response = requests.post(url, request_json)
    new_id = response.json()['id']
    yield new_id
    requests.delete(f"{url}/{new_id}")


# Testing GET request
def test_get_request():
    url = "https://dogapi.dog/api/v2/breeds?page[number]=1&page[size]=5"
    response = requests.get(url)
    json_response = json.loads(response.text)
    name = jsonpath.jsonpath(json_response, "data[0].attributes.name")
    assert name[0] == "Affenpinscher"

#Testing POST request
def test_post_request():
    url = "https://69b675b7583f543fbd9dc80a.mockapi.io/testproject/users"

    f = open("C:\\Users\\Felhasználó\\Documents\GitHub\\API testing\\user.json", "r")
    request_stream = f.read()
    request_json = json.loads(request_stream)
    response = requests.post(url, request_json)
    assert response.status_code == 201

# Testing DELETE request
def test_delete_request(user_id):
    url = f"https://69b675b7583f543fbd9dc80a.mockapi.io/testproject/users/{user_id}"
    delete_response = requests.delete(url)
    assert delete_response.status_code == 200

#Testing PUT request
def test_put_request(user_id):
    url = f"https://69b675b7583f543fbd9dc80a.mockapi.io/testproject/users/{user_id}"

    response = requests.put(url, {"name":"Terry Update","address":"Update City"})
    assert response.status_code == 200
    assert response.json()['name'] == "Terry Update"