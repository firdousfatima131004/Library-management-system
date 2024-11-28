# Library Management System

## Overview
This project is a **Library Management System** built using Python, SQLAlchemy, and SQLite. It provides functionality for managing books, members, and book transactions such as issuing and returning books. The application includes an intuitive console interface with user-friendly prompts and color-coded outputs for better readability.

## Features

1. **Add New Books**
   - Add new books to the library by providing title, author, ISBN, and the number of copies.

2. **View Available Books**
   - View all books in the library, including details like title, author, ISBN, and availability status.

3. **Add New Members**
   - Register new members with their name and email.

4. **View Members**
   - List all registered members with their details.

5. **Issue Books**
   - Issue books to members if they are available.

6. **Return Books**
   - Mark books as returned and update stock.

7. **View Transactions**
   - View all book transactions for a specific member, including issue and return details.

8. **Delete Book Stock**
   - Mark all copies of a book as unavailable.

9. **Exit**
   - Exit the application.

## Project Structure

```
Library Management System
├── main.py        # Main application logic
├── crud.py        # CRUD operations for books, members, and transactions
├── models.py      # SQLAlchemy models for database tables
├── database.py    # Database configuration and session setup
└── Library.db     # SQLite database file (created automatically)
```

## Installation

1. Clone the repository or download the project files.
   ```bash
   git clone https://github.com/your-repo/library-management-system.git
   cd library-management-system
   ```

2. Install the required dependencies:
   ```bash
   pip install pyfiglet colorama sqlalchemy
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Dependencies

- **Python 3.7+**
- **SQLAlchemy**: For ORM and database operations.
- **SQLite**: Backend database.
- **Colorama**: For color-coded console outputs.
- **PyFiglet**: For ASCII art in the console.

## Usage

1. Run the application using the command `python main.py`.
2. Select options from the menu to perform desired actions:
   - Add books or members.
   - View existing books or members.
   - Issue or return books.
   - View transactions for a specific member.
   - Delete book stock.
3. Follow the prompts to enter the required details.
4. Exit the application by choosing option `9`.

## Database Schema

### Books Table (`books`)
| Column   | Type    | Description          |
|----------|---------|----------------------|
| id       | Integer | Primary Key          |
| title    | String  | Title of the book    |
| author   | String  | Author of the book   |
| isbn     | String  | ISBN number          |
| count    | Integer | Number of copies     |

### Members Table (`members`)
| Column   | Type    | Description          |
|----------|---------|----------------------|
| id       | Integer | Primary Key          |
| name     | String  | Name of the member   |
| email    | String  | Unique email address |

### Transactions Table (`transactions`)
| Column       | Type    | Description                    |
|--------------|---------|--------------------------------|
| id           | Integer | Primary Key                    |
| book_id      | Integer | Foreign Key to books table     |
| member_id    | Integer | Foreign Key to members table   |
| issue_date   | Date    | Date the book was issued       |
| return_date  | Date    | Date the book was returned     |

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Colorama Documentation](https://pypi.org/project/colorama/)
- [PyFiglet Documentation](https://pypi.org/project/pyfiglet/)
