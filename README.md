
# Library Manager

Library Manager is a console application designed to manage a library of books. It allows you to add, remove, search for books, update their status, and view the list of all available books. The application saves data to a JSON file, enabling continued use even after restarting the program.

## Key Features

1. **Add Books**  
   Add a new book to the library by specifying its title, author, and year of publication. Each book is automatically assigned a unique identifier (UUID).

2. **Remove Books**  
   Remove a book from the library by providing its unique ID.

3. **Search Books**  
   Search for books by title or author using a search query. The search is case-insensitive.

4. **View All Books**  
   Display the full list of books, showing their current status: either available or borrowed.

5. **Update Book Status**  
   Update the status of a book to available or borrowed by specifying its ID.

6. **Save and Load Data**  
   The library is saved to the library.json file. Upon startup, the data is automatically loaded, allowing you to continue working with the library.

## How It Works

1. Upon starting the program, the main menu is displayed with six options:
   - Add a book.
   - Remove a book.
   - Search for books.
   - Display all books.
   - Update book status.
   - Quit the program.

2. The user selects an option and provides input. For example:
   - When adding a book, the user enters its title, author, and year.
   - When updating the status, the user provides the book's ID and new status.

3. All actions are logged in the library.log file, including adding, removing, and error events.

4. When the user exits the program, the data is automatically saved in the library.json file, so it can be loaded during the next run.

## Example Usage

### Adding a Book
Enter title: 1984
Enter author: George Orwell
Enter year: 1949
Book added with ID: c2a9ff44-5e22-4cfb-bb70-08d57e3f6dc2

### Searching for a Book
Enter search query: Orwell
[3f5c1f2a-a4e8-4bd8-bb70-08d57e3f6dc2] 1984 by George Orwell (1949) - available

### Updating Book Status
Enter book ID to update: 3f5c1f2a-a4e8-4bd8-bb70-08d57e3f6dc2
Enter new status (available/borrowed): borrowed
Book status updated successfully.


## Installation and Running the Application

### Requirements
- Python 3.8 or higher.

### Installation
1. Clone the repository:
   '''bash
   git clone https://github.com/Legeboojka/library-manager.git
   cd library-manager
   

2. (Recommended) Create a virtual environment:
   '''bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   

3. Run the application:
   '''bash
   python main.py
   

## Logging

The application logs events to the library.log file, including successful operations and errors. This makes it easier to diagnose issues if they arise.


## Testing

To run the tests and verify the functionality of the components, use the following command:
'''bash
python -m unittest discover tests


## License

This project is licensed under the MIT License. You are free to use and modify the code.

