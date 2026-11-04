import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

# GET /USERS/NEW
# status code test
def test_get_signup_form_returns_a_200():
    client = app.test_client()
    response = client.get("/users/new")
    assert response.status_code == 200

# GET /SESSIONS/NEW
# status code test
def test_get_login_form_returns_a_200():
    client = app.test_client()
    response = client.get("/sessions/new")
    assert response.status_code == 200

# GET /BOOKS
# status code test
def test_get_books_returns_a_200():
    client = app.test_client()
    response = client.get("/books")
    assert response.status_code == 200

# GET /films
#status code test
def test_get_films_returns_a_200():
    client = app.test_client()
    response = client.get("/films")
    assert response.status_code == 200

# GET /AUTHORS
# status code test
def test_get_authors_returns_a_200():
    client = app.test_client()
    response = client.get("/authors")
    assert response.status_code == 200

# GET /quotes
# status code test
def test_get_quotes_returns_a_200():
    client = app.test_client()
    response = client.get("/quotes")
    assert response.status_code == 200

"""
# response body test - rewrite for HTML
def test_get_quotes_returns_all_quotes():
    client = app.test_client()
    response = client.get("/quotes")
    assert response.json == [
        "If one cannot enjoy reading a book over and over again, there is no use in reading it at all - Oscar Wilde",
        "A reader lives a thousand lives before he dies, a man who never reads lives only one - George R R Martin",
        "There is no friend as loyal as a book - Ernest Hemmingway"
    ]
"""