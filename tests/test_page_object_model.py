import pytest
from playwright.sync_api import expect
from playwright.sync_api import Page

class Login:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("#username")
        self.passoword_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name = " Login")
        self.text_match = page.locator(".subheader")
        self.error_alert = page.locator("#flash")


    def goto(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, email, password):
        self.email_input.fill(email)
        self.passoword_input.fill(password)
        self.login_button.click()
        
def test_login_valid_credentials(page: Page):
    login_page =  Login(page)
    login_page.goto()
    login_page.login("tomsmith", "SuperSecretPassword!")
    expect(login_page.text_match).to_have_text("Welcome to the Secure Area. When you are done click logout below.")



def test_login_with_invalid_password(page: Page):
    login_page = Login(page)
    login_page.goto()
    login_page.login("tomsmith", "wrong-password")
    expect(login_page.error_alert).to_have_text(" Your username is invalid! ")