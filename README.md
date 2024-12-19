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
