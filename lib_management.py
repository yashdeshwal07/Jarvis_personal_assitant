class Book:
    def __init__(self, t, a, i):
        self.title = t
        self.author = a
        self.isbn = i
        self.availability = True
        self.borrowed_by = None

    def display_info(self):
        if self.availability:
            print(
                f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"ISBN: {self.isbn}\n"
                f"Availability: Available"
            )
        else:
            print(
                f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"ISBN: {self.isbn}\n"
                f"Availability: Borrowed by ID: {self.borrowed_by}"
            )


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.title in self.books:
            print("Book already exists")
        else:
            self.books[book.title] = book
            print(f"'{book.title}' added in Library")

    def display_books(self):
        for items in self.books:
            self.books[items].display_info()
            print("-" * 30)

    def search_book(self, title):
        if title in self.books:
            self.books[title].display_info()
        else:
            print("Book not in Library")

    def borrow_book(self, title, user_id):
        if title in self.books:
            if self.books[title].availability:
                print(f"You have borrowed the book '{title}'")
                self.books[title].availability = False
                self.books[title].borrowed_by = user_id
                return True
            else:
                print("Book already borrowed")
                return False
        else:
            print("Book not in Library")

    def return_book(self, book):
        if book in self.books:
            if not self.books[book].availability:
                print(f"You have returned the book '{book}'")
                self.books[book].availability = True
                return True
        else:
            print("Book not in Library")

    def remove_book(self, t):
        if t in self.books:
            if self.books[t].availability:
                del self.books[t]
                print("Successfully removed")
            else:
                print("Book is borrowed")
        else:
            print("Book already not in library")


class User:
    max_borrowing_limit = 2

    def __init__(self, n, i):
        self.name = n
        self.id = i
        self.borrowed_books = []
        all_users[self.id] = self

    def borrow_book(self, lib, title):
        if len(self.borrowed_books) < self.max_borrowing_limit:
            if lib.borrow_book(title, self.id):
                self.borrowed_books.append(title)
        else:
            print("You have reached you borrowing limit")

    def return_book(self, lib, title):
        if title not in self.borrowed_books:
            print("This book was not borrowed by you")
        elif lib.return_book(title):
            self.borrowed_books.remove(title)

    def display_borrowed_books(self):
        print(self.borrowed_books)


all_users = {}

b1 = Book("Harry Potter", "JK Rowling", "2025UCA001")
b2 = Book("Fantastic Beasts", "JK Rowling", "2025UCA002")
b3 = Book("Python Basics", "Guido", "2025UCA003")

l1 = Library()

u1 = User("User1", 101)
u2 = User("User2", 102)

l1.add_book(b1)
l1.add_book(b2)
l1.add_book(b3)


def menu():
    print("\n1. Add book in library")
    print("2. Display all books in library")
    print("3. Search book in library")
    print("4. Remove book from library")
    print("5. Borrow book")
    print("6. Return book")
    print("7. Display books borrowed by you")
    print("8. Exit")


while True:
    try:
        menu()
        user = int(input())

        if user == 1:
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter isbn: ")
            l1.add_book(Book(title, author, isbn))

        elif user == 2:
            l1.display_books()

        elif user == 3:
            title = input("Enter book title: ")
            l1.search_book(title)

        elif user == 4:
            title = input("Enter book title: ")
            l1.remove_book(title)

        elif user == 5:
            user_id = int(input("Enter you ID: "))
            if user_id in all_users:
                title = input("Enter book title: ")
                all_users[user_id].borrow_book(l1, title)
            else:
                print("You are not a registered user")

        elif user == 6:
            user_id = int(input("Enter you ID: "))
            if user_id in all_users:
                title = input("Enter book title: ")
                all_users[user_id].return_book(l1, title)
            else:
                print("You are not a registered user")

        elif user == 7:
            user_id = int(input("Enter you ID: "))
            if user_id in all_users:
                all_users[user_id].display_borrowed_books()
            else:
                print("You are not a registered user")

        elif user == 8:
            break

        else:
            print("Type between 1-8")

    except ValueError:
        print("Type between 1-8")
