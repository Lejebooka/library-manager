import json
from typing import List
from .models import Book

class BookStorage:
    """
    Handles loading and saving books to/from a JSON file.
    """

    def __init__(self, filename: str) -> None:
        """
        Initializes the storage with the specified file.
        """
        self.filename = filename

    def load_books(self) -> List[Book]:
        """
        Loads a list of books from the JSON file.
        """
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)  
                print(f"Successfully loaded books from '{self.filename}'.")
                return [Book.from_dict(book) for book in data]  
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Returning an empty list.")
            return []
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON from '{self.filename}': {e}")
            return []

    def save_books(self, books: List[Book]) -> None:
        """
        Saves a list of books to the JSON file.
        """
        try:
            with open(self.filename, "w") as file:
                json.dump([book.to_dict() for book in books], file, indent=4, ensure_ascii=False)
                print(f"Books successfully saved to '{self.filename}'.")
        except IOError as e:
            print(f"Failed to write to file '{self.filename}': {e}")
