from pages.login_page import LoginPage
from utils.config import LOGIN_URL, USERNAME, PASSWORD

def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.navigate(LOGIN_URL)
    login_page.login(USERNAME, PASSWORD)

    assert "dashboard" in page.url.lower()
