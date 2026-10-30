class Film:
    def __init__(self, title, genre, id = None):
        self.id = id
        self.title = title
        self.genre = genre
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    def __repr__(self):
        return f"{self.title}, {self.genre}"