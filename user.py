class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                return True
        return False

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"User: {self.name}, Borrowed Books: {borrowed_titles}"
