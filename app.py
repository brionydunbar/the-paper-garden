from flask import Flask, render_template, request, redirect, session
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book
from lib.film_repository import FilmRepository
from lib.film import Film
from lib.user_repository import UserRepository
from lib.user import User
from login_required import login_required

app = Flask(__name__)
app.secret_key = "some_really_secret_key"

# LANDING PAGE
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# USERS
# GET /USERS/NEW
@app.route("/users/new", methods=["GET"])
def get_signup_form():
    return render_template("signup_form.html")

# POST /USERS
@app.route("/users", methods=["POST"])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form
    user = User(username=user_details["username"], password=user_details["password"])
    user_repository.create(user)
    return redirect("/")

# SESSIONS
# GET /SESSIONS/NEW
@app.route("/sessions/new", methods=["GET"])
def get_login_form():
    return render_template("login_form.html")

# POST SESSIONS
@app.route("/sessions", methods=["POST"])
def create_session():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    username = request.form["username"]
    password = request.form["password"]
    user = user_repository.find(username)
    if user and user.password == password:
        session["user_id"] = user.id
        session["username"] = user.username
        return redirect("/")
    else:
        return redirect("/sessions/new")

# BOOKS
# GET /BOOKS - dynamic
@app.route('/books', methods=['GET'])
def get_all_books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    print(books)
    return render_template("books.html", books=books)

# POST /books
@app.route('/books', methods=['POST'])
@login_required
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book_details = request.form
    book = Book(title=book_details["title"], author=book_details["author"])
    book_repository.create(book)
    return redirect("/books")


# FILMS
# GET /films - dynamic
@app.route("/films", methods=["GET"])
def get_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    films = film_repository.all()
    return render_template("films.html", films=films)

# POST /films
@app.route('/films', methods=['POST'])
def create_film():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    film_details = request.form
    film = Film(title=film_details["title"], genre=film_details["genre"])
    film_repository.create(film)
    return redirect("/films")

# AUTHORS
# GET /AUTHORS - hardcoded
@app.route("/authors", methods=["GET"])
def author_list():
    author_list = [
        {"name": "Julia Donaldson",
        "dob": "1948-09-16"},
        {"name": "Andrea Beaty",
        "dob": "1961-10-08"},
        {"name": "Kelly Barnhill",
        "dob": "1973-01-01"},
        {"name": "Zetta Elliott",
        "dob": "1979-11-11"}
        ]
    return render_template("authors.html", authors=author_list)


# QUOTES
# GET /QUOTES - hardcoded
@app.route("/quotes", methods=["GET"])
def quote_list():
    quote_list = [
        "If one cannot enjoy reading a book over and over again, there is no use in reading it at all - Oscar Wilde",
        "A reader lives a thousand lives before he dies, a man who never reads lives only one - George R R Martin",
        "There is no friend as loyal as a book - Ernest Hemmingway"
    ]
    return render_template("/quotes.html", quotes=quote_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)