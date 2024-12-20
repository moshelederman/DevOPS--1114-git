#Exercise: Understanding a Python Library System
#Objective:
#Read the given code and answer questions about its functionality.
#Code:
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Copies: {self.copies}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def __str__(self):
        return str(self.books)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

# Example Usage
library = Library()
library.add_book(Book("Python 101", "John Doe", 3))
library.add_book(Book("Data Science Handbook", "Jane Smith", 5))
library.list_books()


found_book = library.find_book_by_title("moshe 101")
if found_book:
    print(f"Book found: {found_book}")
else:
    print("Book not found")    

#Questions:
#1. Classes and Attributes:
#- What is the purpose of the `Book` class? What attributes does it have?
#A the purpose of the 'book' is to present book in library. does have 3 attributes: title, authe and copies.
#- What is the purpose of the `Library` class? What does its `books` attribute store?
#A the purpose of the 'library' is to present library with list of books.does have 1 attribute:books.

#2. Methods:
#- What does the `add_book` method do?
#A the `add_book` method do add book to the list of books in library. 
#- What happens when the `list_books` method is called?
#A the `list_books` method do print the list of books in library.

#3. Behavior Analysis:
#- What is the output of the `list_books` method after the books are added?
#A the output of the `list_books` method after the books are added is:
#  Title: Python 101, Author: John Doe, Copies: 3
#  Title: Data Science Handbook, Author: Jane Smith, Copies: 5
#- What happens if you call `add_book` with a new book object?
#A the new book object add to the list of books' when i call `list_books` method it will apear.
#  
#4. Code Change:
#- If you wanted to add a method to find a book by title in the library, how would you do it?
#A I write the new method up. 