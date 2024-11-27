import unittest
from library.models import Book

class TestBook(unittest.TestCase):
    def test_create_book(self):
        book = Book("1984", "George Orwell", 1949)
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George Orwell")
        self.assertEqual(book.year, 1949)
        self.assertEqual(book.status, "available")
        self.assertIsNotNone(book.id)

    def test_to_dict(self):
        book = Book("1984", "George Orwell", 1949)
        book_dict = book.to_dict()
        self.assertEqual(book_dict["title"], "1984")
        self.assertEqual(book_dict["author"], "George Orwell")

    def test_from_dict(self):
        data = {
            "title": "1984",
            "author": "George Orwell",
            "year": 1949,
            "status": "available"
        }
        book = Book.from_dict(data)
        self.assertEqual(book.title, "1984")

if __name__ == "__main__":
    unittest.main()
