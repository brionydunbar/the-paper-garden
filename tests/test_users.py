from app import app
from lib.database_connection import DatabaseConnection
from playwright.async_api import Page
from werkzeug.security import generate_password_hash

def test_create_user_is_saved_to_database():
    # create the test client to send requests without using Playwright and a browser
    client = app.test_client()
    # set up a DB connection
    connection = DatabaseConnection()
    connection.connect()
    # use execute to send a TRUNCATE TABLE query
    connection.execute("TRUNCATE TABLE users;")
    # send the request
    response = client.post('/users', data={
        'username': 'testuser',
        'password': 'password123'
    })
    # assert that the redirect happened
    assert response.status_code == 302
    # read from the DB
    result = connection.execute("SELECT * FROM users WHERE username = 'testuser'")
    # assert that the user was created
    assert len(result) == 1
    assert result[0]['username'] == 'testuser'

def test_signup_redirects_to_login(page: Page):
    page.goto("http://127.0.0.1:5001/users/new")
    page.get_by_label("Username").fill("test")
    page.get_by_label("Password").fill("1234")
    page.get_by_role("button").click()

    assert page.url == "http://127.0.0.1:5001/sessions/new"