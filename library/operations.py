from typing import List, Optional
from .models import Book


class LibraryOperations:
    """
    Class to manage a collection of books with operations such as adding,
    removing, searching, and updating book statuses.
    """

    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, title: str, author: str, year: int) -> Book:
        """
        Adds a new book to the library.
        """
        book = Book(title=title, author=author, year=year)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")
        return book

    def remove_book(self, book_id: str) -> Optional[Book]:
        """
        Removes a book from the library based on its ID.
        """
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                print(f"Book '{book.title}' by {book.author} removed from the library.")
                return book
        raise ValueError("Book ID not found.")

    def search_books(self, query: str) -> List[Book]:
        """
        Searches for books in the library by title or author.
        """
        query = query.lower()
        results = [
            book for book in self.books
            if query in book.title.lower() or query in book.author.lower()
        ]
        print(f"Found {len(results)} book(s) matching the query '{query}'.")
        return results

    def update_status(self, book_id: str, status: str) -> Book:
        """
        Updates the status of a book based on its ID.
        """
        if status not in ["available", "borrowed"]:
            raise ValueError("Invalid status. Allowed values are 'available' or 'borrowed'.")

        for book in self.books:
            if book.id == book_id:
                book.status = status
                print(f"Status of book '{book.title}' updated to '{status}'.")
                return book
        raise ValueError("Book ID not found.")
