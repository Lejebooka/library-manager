import uuid
from typing import Dict, Union

class Book:
    def __init__(self, title: str, author: str, year: int, status: str = "available") -> None:
        """
        Initializing a book with an automatically generated ID.
        """
        self.id: str = str(uuid.uuid4())
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = status

    def to_dict(self) -> Dict[str, Union[str, int]]:
        """
        Converting a book object to a dictionary.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: Dict[str, Union[str, int]]) -> "Book":
        """
        Creating a book object from a dictionary.
        """
        return Book(
            title=str(data["title"]),
            author=str(data["author"]),
            year=int(data["year"]),
            status=str(data.get("status", "available")),
        )
