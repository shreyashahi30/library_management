from flask import Blueprint, request, jsonify
from app.services.book_service import BookService
from app.auth import token_required

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['POST'])
@token_required
def create_book():
    data = request.json
    if 'title' not in data or 'author' not in data:
        return jsonify({"error": "Invalid data"}), 400
    book = BookService.create_book(data['title'], data['author'])
    return jsonify(book), 201

@books_bp.route('/books', methods=['GET'])
@token_required
def list_books():
    title = request.args.get('title')
    author = request.args.get('author')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))
    books, total = BookService.list_books(page, per_page, title, author)
    return jsonify({"books": books, "total": total, "page": page, "per_page": per_page})

