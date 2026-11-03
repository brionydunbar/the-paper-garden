class Book:
    def __init__(self, title, author, synopsis, rating, notes, id = None):
        self.id = id
        self.title = title
        self.author = author
        self.synopsis = synopsis
        self.rating = rating
        self.notes = notes

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.title} by {self.author}"