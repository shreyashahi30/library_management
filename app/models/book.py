from app.models.base_model import BaseModel

class Book(BaseModel):
    def search(self, title=None, author=None):
        results = []
        for book in self.data.values():
            if (title and title.lower() in book['title'].lower()) or \
               (author and author.lower() in book['author'].lower()):
                results.append(book)
        return results

book_model = Book()

