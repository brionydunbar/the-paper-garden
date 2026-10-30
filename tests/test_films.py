from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

def test_films_has_heading(page: Page):
    page.goto("http://127.0.0.1:5001/films")
    h1 = page.locator("h1")
    expect(h1).to_have_text("The Film Corner")

def test_list_of_films_has_all_films(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/book_store.sql")
    page.goto("http://127.0.0.1:5001/films")
    li = page.get_by_role("listitem")
    expect(li).to_have_text(["The Grand Budapest Hotel, Comedy", 
        "Interstellar, Sci-Fi", 
        "Get Out, Horror"])

def test_create_posts_film_to_database(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/book_store.sql")
    page.goto("http://127.0.0.1:5001/films")
    page.get_by_label("Title").fill("(500) Days of Summer")
    page.get_by_label("Genre").fill("Rom-Com")
    page.get_by_role("button", name="Add film").click()
    films = page.locator("li")
    new_film = films.all_inner_texts()[-1]
    assert new_film == "(500) Days of Summer, Rom-Com"