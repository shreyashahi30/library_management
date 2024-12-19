import unittest
from app.models.book import book_model

class TestBookModel(unittest.TestCase):
    def test_create_book(self):
        book = book_model.create({"title": "1984", "author": "George Orwell"})
        self.assertEqual(book["title"], "1984")
        self.assertEqual(book["author"], "George Orwell")

