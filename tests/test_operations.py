import unittest
from library.models import Book
from library.operations import LibraryOperations


class TestLibraryOperations(unittest.TestCase):
    def setUp(self):
        self.library = LibraryOperations()

    def test_add_book(self):
        book = self.library.add_book("Dune", "Frank Herbert", 1965)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.title, "Dune")
        self.assertEqual(book.author, "Frank Herbert")
        self.assertEqual(book.year, 1965)
        self.assertEqual(len(self.library.books), 1)

    def test_remove_book(self):
        book = self.library.add_book("Dune", "Frank Herbert", 1965)
        removed_book = self.library.remove_book(book.id)
        self.assertEqual(removed_book, book)
        self.assertEqual(len(self.library.books), 0)

        with self.assertRaises(ValueError):
            self.library.remove_book("nonexistent_id")

    def test_search_books(self):
        self.library.add_book("Dune", "Frank Herbert", 1965)
        self.library.add_book("Foundation", "Isaac Asimov", 1951)

        results = self.library.search_books("Dune")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Dune")

        results = self.library.search_books("Asimov")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "Isaac Asimov")

        results = self.library.search_books("Nonexistent")
        self.assertEqual(len(results), 0)

    def test_update_status(self):
        book = self.library.add_book("Dune", "Frank Herbert", 1965)
        updated_book = self.library.update_status(book.id, "borrowed")
        self.assertEqual(updated_book.status, "borrowed")

        with self.assertRaises(ValueError):
            self.library.update_status(book.id, "invalid_status")

        with self.assertRaises(ValueError):
            self.library.update_status("nonexistent_id", "available")


if __name__ == "__main__":
    unittest.main()
