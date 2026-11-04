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

def test_book_by_id_has_correct_information(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/book_store.sql")
    page.goto("http://127.0.0.1:5001/books/1")
    expect(page.get_by_role("heading", name="The Gruffalo")).to_be_visible()

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
    page.get_by_role("link", name="Add a book").click()
    
    page.goto("http://127.0.0.1:5001/books/new")
    page.get_by_label("Title").fill("The Chronicles of Geronimo (the cat)")
    page.get_by_label("Author").fill("Geronimo")
    page.get_by_label("Synopsis").fill("A curious and adventurous cat named Geronimo embarks on a series of unexpected adventures, exploring the world beyond his familiar surroundings, encountering new friends and getting into all sorts of mischief along the way.")
    page.get_by_label("Rating (0 - 5 stars)").fill("4")
    page.get_by_label("Notes").fill("This is a fictional work of fiction.")
    with page.expect_response(lambda response: "/books" in response.url and response.request.method == "POST") as response_info:
        page.get_by_role("button", name="Add book").click()
    books = page.locator("li")
    new_book = books.all_inner_texts()[-1]
    assert new_book == "The Chronicles of Geronimo (the cat) by Geronimo"

# unauthorised
def test_unauth_user_cannot_access_new_book_page(page: Page):
    page.goto("http://127.0.0.1:5001/books/new")
    assert "/sessions/new" in page.url
    assert "next=/books/new" in page.url

def test_unauth_user_cannot_post_book_to_database(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/book_store.sql")
    connection.execute("TRUNCATE TABLE users;")

    response = page.request.post(
        "http://127.0.0.1:5001/books",
        form={
            "title": "The Chronicles of Geronimo (the cat)",
            "author": "Geronimo",
            "synopsis": "A curious cat goes on adventures.",
            "rating": "4",
            "notes": "A fictional work."
        }
    )

    assert response.status == 200
    assert response.url == "http://127.0.0.1:5001/sessions/new?next=/books"