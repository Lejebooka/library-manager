import logging
from library.storage import BookStorage
from library.operations import LibraryOperations
from library.models import Book
from typing import List

FILENAME: str = "library.json"


logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main() -> None:
    """
    Main function to manage the library system.
    """
    storage: BookStorage = BookStorage(FILENAME)
    operations: LibraryOperations = LibraryOperations()
    operations.books = storage.load_books()

    while True:
        print("\n*** Library Manager ***")
        print("1) Add a book")
        print("2) Remove a book")
        print("3) Search books")
        print("4) Display all books")
        print("5) Update book status")
        print("6) Quit")
        
        choice: str = input("Choose an option >>> ").strip()

        try:
            if choice == "1":
                title: str = input("Enter title: ")
                author: str = input("Enter author: ")
                year: int = int(input("Enter year: "))
                book: Book = operations.add_book(title, author, year)
                logging.info(f"Added book: {book.title} by {book.author}.")
                print(f"Book added with ID: {book.id}")

            elif choice == "2":
                book_id: str = input("Enter book ID to remove: ")
                operations.remove_book(book_id)
                logging.info(f"Removed book with ID: {book_id}")
                print("Book removed successfully.")

            elif choice == "3":
                query: str = input("Enter search query: ")
                results: List[Book] = operations.search_books(query)
                for book in results:
                    print(f"[{book.id}] {book.title} by {book.author} ({book.year}) - {book.status}")
                if not results:
                    print("No books found.")

            elif choice == "4":
                for book in operations.books:
                    print(f"[{book.id}] {book.title} by {book.author} ({book.year}) - {book.status}")
                if not operations.books:
                    print("No books in the library.")

            elif choice == "5":
                book_id: str = input("Enter book ID to update: ")
                status: str = input("Enter new status (available/borrowed): ")
                operations.update_status(book_id, status)
                logging.info(f"Updated status for book with ID: {book_id} to {status}")
                print("Book status updated successfully.")

            elif choice == "6":
                storage.save_books(operations.books)
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            logging.error(f"Error: {e}")
            print(f"Error: {e}")

if __name__ == "__main__":
    main() 
