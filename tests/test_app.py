import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

# GET /BOOKS
# status code test
def test_get_books_returns_a_200():
    # here's where we make the test client
    client = app.test_client()
    # here's where we make the request
    response = client.get("/books")
    # here's where we assert that the response's status code is 200
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

# response body test - rewrite for HTML
"""
def test_get_authors_returns_all_authors():
    client = app.test_client()
    response = client.get("/authors")
    assert response.json == [
        {
            "name": "Julia Donaldson",
            "dob": "1948-09-16"
        },
        {
            "name": "Andrea Beaty",
            "dob": "1961-10-08"
        },
        {
            "name": "Kelly Barnhill",
            "dob": "1973-01-01"
        },
        {
            "name": "Zetta Elliott",
            "dob": "1979-11-11"
        }
        ]
"""

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