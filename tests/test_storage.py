import unittest
import os
from library.models import Book
from library.storage import BookStorage

class TestBookStorage(unittest.TestCase):
    def setUp(self):
        self.filename = "test_library.json"
        self.storage = BookStorage(self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_and_load_books(self):
        books = [
            Book(title="1984", author="George Orwell", year=1949),
            Book(title="Brave New World", author="Aldous Huxley", year=1932),
        ]
        self.storage.save_books(books)
        loaded_books = self.storage.load_books()
        self.assertEqual(len(loaded_books), 2)
        self.assertEqual(loaded_books[0].title, "1984")
        self.assertEqual(loaded_books[1].author, "Aldous Huxley")

    def test_load_books_file_not_found(self):
        loaded_books = self.storage.load_books()
        self.assertEqual(loaded_books, [])

if __name__ == "__main__":
    unittest.main()
