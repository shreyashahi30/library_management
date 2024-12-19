# Library Management System

An advanced Flask-based Library Management System implementing modular design, token-based authentication, in-memory database abstraction, and comprehensive error handling.

## Features

- **Modular and Scalable Architecture**: Separation of concerns with models, services, and routes for easy extensibility.
- **Token-Based Authentication**: Middleware for secure API access.
- **Dynamic Pagination**: Supports filtering, sorting, and paginated data retrieval.
- **Custom Error Handling**: Centralized and user-friendly error responses.
- **Unit Testing**: Comprehensive test coverage for key components.

---

## Project Structure

```plaintext
library_management/
├── app/
│   ├── __init__.py         # Flask app initialization
│   ├── models/             # Data models
│   │   ├── base_model.py   # Base model abstraction
│   │   ├── book.py         # Book model
│   │   ├── member.py       # Member model
│   ├── services/           # Business logic layer
│   │   ├── book_service.py # Book services
│   │   ├── member_service.py # Member services
│   ├── routes/             # API routes
│   │   ├── books.py        # Book routes
│   │   ├── members.py      # Member routes
│   ├── auth.py             # Token-based authentication middleware
│   ├── error_handlers.py   # Custom error handling
│   ├── utils.py            # Helper functions
├── tests/                  # Unit tests
│   ├── test_books.py       # Book model tests
│   ├── test_members.py     # Member model tests
│   ├── test_auth.py        # Authentication tests
├── app.py                  # Main application entry point
└── README.md               # Documentation
```plaintext
## Setup Instructions

### Prerequisites
- Python 3.8 or later installed on your system.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/library-management-system.git
    cd library-management-system
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install flask
    ```

4. Run the application:

    ```bash
    python app.py
    ```

    The app will run on `http://127.0.0.1:5000`.

### API Endpoints

#### Authentication
All routes require a valid token:
- **Header**: `Authorization: secure_token`

#### Books
| Method | Endpoint            | Description                           |
|--------|---------------------|---------------------------------------|
| POST   | /api/books           | Add a new book.                       |
| GET    | /api/books           | List all books with pagination.       |
| GET    | /api/books/<id>      | Get details of a specific book.       |
| PUT    | /api/books/<id>      | Update an existing book.              |
| DELETE | /api/books/<id>      | Delete a book.                        |

#### Members
| Method | Endpoint            | Description                           |
|--------|---------------------|---------------------------------------|
| POST   | /api/members         | Add a new member.                     |
| GET    | /api/members         | List all members with pagination.     |
| GET    | /api/members/<id>    | Get details of a specific member.     |
| PUT    | /api/members/<id>    | Update an existing member.            |
| DELETE | /api/members/<id>    | Delete a member.                      |

### Testing
Run tests using `unittest`:

```bash
python -m unittest discover tests
