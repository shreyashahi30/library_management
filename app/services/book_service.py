from app.models.book import book_model

class BookService:
    @staticmethod
    def create_book(title, author):
        return book_model.create({"title": title, "author": author})

    @staticmethod
    def list_books(page, per_page, title=None, author=None):
        books = book_model.search(title, author)
        start = (page - 1) * per_page
        end = start + per_page
        return books[start:end], len(books)

    @staticmethod
    def get_book(book_id):
        return book_model.get_by_id(book_id)

    @staticmethod
    def update_book(book_id, title, author):
        return book_model.update(book_id, {"title": title, "author": author})

    @staticmethod
    def delete_book(book_id):
        return book_model.delete(book_id)

