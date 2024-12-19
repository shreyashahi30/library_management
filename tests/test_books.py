import unittest
from app.models.book import book_model
from app.services.book_service import BookService


class TestBookService(unittest.TestCase):
    def setUp(self):
        self.service = BookService
        # Clear the book model before each test
        book_model.data.clear()
        book_model.counter = 1

    def test_create_book(self):
        book = self.service.create_book("1984", "George Orwell")
        self.assertEqual(book["title"], "1984")
        self.assertEqual(book["author"], "George Orwell")
        self.assertIn("id", book)

    def test_list_books(self):
        self.service.create_book("1984", "George Orwell")
        self.service.create_book("To Kill a Mockingbird", "Harper Lee")
        books, total = self.service.list_books(1, 2)
        self.assertEqual(len(books), 2)
        self.assertEqual(total, 2)

    def test_search_books(self):
        self.service.create_book("1984", "George Orwell")
        self.service.create_book("Animal Farm", "George Orwell")
        results = book_model.search(title="1984")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "1984")

    def test_update_book(self):
        book = self.service.create_book("1984", "George Orwell")
        updated = self.service.update_book(book["id"], "1984 Updated", "G. Orwell")
        self.assertEqual(updated["title"], "1984 Updated")
        self.assertEqual(updated["author"], "G. Orwell")

    def test_delete_book(self):
        book = self.service.create_book("1984", "George Orwell")
        deleted = self.service.delete_book(book["id"])
        self.assertEqual(deleted["title"], "1984")
        self.assertIsNone(book_model.get_by_id(book["id"]))


if __name__ == "__main__":
    unittest.main()
