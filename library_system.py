from book import Book
from user import User

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Book '{title}' added to the library.")

    def add_user(self, user_id, name):
        new_user = User(user_id, name)
        self.users.append(new_user)
        print(f"User '{name}' added to the system.")

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def borrow_book(self, user_id, isbn):
        user = self.find_user(user_id)
        book = self.find_book(isbn)

        if user and book:
            if user.borrow_book(book):
                print(f"User '{user.name}' borrowed '{book.title}'.")
            else:
                print(f"Book '{book.title}' is already borrowed.")
        else:
            print("Invalid user or book.")

    def return_book(self, user_id, isbn):
        user = self.find_user(user_id)
        book = self.find_book(isbn)

        if user and book:
            if user.return_book(book):
                print(f"User '{user.name}' returned '{book.title}'.")
            else:
                print(f"Book '{book.title}' was not borrowed by '{user.name}'.")
        else:
            print("Invalid user or book.")

    def list_available_books(self):
        for book in self.books:
            if not book.is_borrowed:
                print(book)

    def list_borrowed_books(self):
        for book in self.books:
            if book.is_borrowed:
                print(book)


# Sample Usage
if __name__ == "__main__":
    library = LibrarySystem()

    # Add some books
    library.add_book("Python Programming", "John Doe", "123456789")
    library.add_book("Data Science with Python", "Jane Smith", "987654321")

    # Add users
    library.add_user(1, "Alice")
    library.add_user(2, "Bob")

    # Borrow a book
    library.borrow_book(1, "123456789")

    # List all available books
    print("\nAvailable Books:")
    library.list_available_books()

    # List all borrowed books
    print("\nBorrowed Books:")
    library.list_borrowed_books()

    # Return a book
    library.return_book(1, "123456789")

    # List all available books again
    print("\nAvailable Books After Return:")
    library.list_available_books()
