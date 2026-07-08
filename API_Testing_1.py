import pytest
import requests
from playwright.sync_api import Page, expect
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


def test_create_and_view_post(page: Page, api_base_url):
    response = requests.post(api_base_url + "/posts", json={"title" :"verify post", "body" :"Furqan verify kar raha hai", "user_id": 2 })
    post_id = response.json()["id"]
    print(post_id)
    page.goto(api_base_url + f"/posts/{post_id}")     
    expect(page).to_have_url(api_base_url + f"/posts/{post_id}")
