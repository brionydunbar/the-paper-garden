from app import app
from lib.database_connection import DatabaseConnection
from playwright.async_api import Page

# successful authentication tests
def test_auth_integration():
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) VALUES ('test', '1234');")
    
    response = client.post("/sessions", data={
        "username": "test",
        "password": "1234"
    })

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")

def test_auth_playwright(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    page.goto("http://127.0.0.1:5001/sessions/new")
    page.get_by_label("Username").fill("test")
    page.get_by_label("Password").fill("1234")
    page.get_by_role("button").click()

    assert page.url == "http://127.0.0.1:5001/"


# failed authentication tests
def test_failed_auth_integration():
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) VALUES ('test', '1234');")
    
    response = client.post("/sessions", data={
        "username": "test1",
        "password": "12345"
    })

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/sessions/new")

def test_failed_auth_playwright(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    page.goto("http://127.0.0.1:5001/sessions/new")
    page.get_by_label("Username").fill("test1")
    page.get_by_label("Password").fill("12345")
    page.get_by_role("button").click()

    assert page.url == "http://127.0.0.1:5001/sessions/new"