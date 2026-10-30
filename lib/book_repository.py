from lib.book import Book

class BookRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all books
    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["title"], row["author"], row["id"])
            books.append(item)
        return books

    # Create a new book
    def create(self, book):
        self._connection.execute('INSERT INTO books (title, author) VALUES (%s, %s)', [book.title, book.author])
        return None