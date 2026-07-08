import pytest
import requests
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print("Status Code: ", response.status_code)
# assert response.status_code == 200
# print(response.json())
# assert response.json()["id"] == 1

@pytest.fixture
def api_base_url():
    return "https://jsonplaceholder.typicode.com"

def test_get_post_returns_correct_data(api_base_url):
    response = requests.get(api_base_url+ "/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_create_post(api_base_url):
    response = requests.post(api_base_url + "/posts", json = {"title": "my post", "body": "Furqan is learning", "userId": 1})
    assert response.status_code == 201
    assert response.json()["title"] == "my post"

def test_get_nonexistent_post(api_base_url):
    response = requests.get(api_base_url + "/posts/99999")
    assert response.status_code == 404



