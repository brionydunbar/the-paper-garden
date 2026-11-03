from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

def test_books_has_heading(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    h1 = page.locator("h1")
    expect(h1).to_have_text("My Bookshelf")

def test_list_of_books_has_all_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/book_store.sql")
    page.goto("http://127.0.0.1:5001/books")
    books = page.locator("li")
    expected_books = [
        'The Gruffalo by Julia Donaldson',
        'Ada Twist, Scientist by Andrea Beaty',
        'The Girl Who Drank the Moon by Kelly Barnhill',
        'Dragons in a Bag by Zetta Elliott'
    ]
    actual_books = books.all_inner_texts()
    assert actual_books == expected_books

# create books tests
# authorised
def test_create_posts_book_to_database(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/book_store.sql")
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    page.goto("http://127.0.0.1:5001/sessions/new")
    page.get_by_placeholder("username").fill("test")
    page.get_by_placeholder("password").fill("1234")
    page.get_by_role("button").click()

    page.goto("http://127.0.0.1:5001/books")
    page.get_by_label("Title").fill("The Chronicles of Geronimo (the cat)")
    page.get_by_label("Author").fill("Geronimo")
    page.get_by_role("button", name="Add book").click()
    books = page.locator("li")
    new_book = books.all_inner_texts()[-1]
    assert new_book == "The Chronicles of Geronimo (the cat) by Geronimo"

# unauthorised
def test_unauth_create_does_not_post_book_to_database(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/book_store.sql")
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    page.goto("http://127.0.0.1:5001/sessions/new")
    page.get_by_placeholder("username").fill("test1")
    page.get_by_placeholder("password").fill("12345")
    page.get_by_role("button").click()

    page.goto("http://127.0.0.1:5001/books")
    page.get_by_label("Title").fill("The Chronicles of Geronimo (the cat)")
    page.get_by_label("Author").fill("Geronimo")
    page.get_by_role("button", name="Add book").click()
    books = page.locator("li")
    new_book = books.all_inner_texts()
    assert new_book == [] # empty list as no book created