import json

def load_books():
    """Load books from a JSON file."""
    try:
        with open("books_data.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books):
    """Save current book collection to JSON file."""
    with open("books_data.json", "w") as f:
        json.dump(books, f, indent=4)

def add_book(books):
    """Add a new book to the collection."""
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    year = input("Enter publication year: ").strip()
    genre = input("Enter genre: ").strip()
    read = input("Mark as read? (yes/no): ").strip().lower() == "yes"
    
    if title and author:
        books.append({"title": title, "author": author, "year": year, "genre": genre, "read": read})
        save_books(books)
        print("Book added successfully!")
    else:
        print("Title and Author are required!")

def delete_book(books):
    """Delete a book from the collection."""
    for i, book in enumerate(books):
        print(f"{i+1}. {book['title']} by {book['author']}")
    
    index = int(input("Enter book number to delete: ")) - 1
    if 0 <= index < len(books):
        books.pop(index)
        save_books(books)
        print("Book deleted successfully!")
    else:
        print("Invalid selection!")

def update_book(books):
    """Update details of an existing book."""
    for i, book in enumerate(books):
        print(f"{i+1}. {book['title']} by {book['author']}")
    
    index = int(input("Enter book number to update: ")) - 1
    if 0 <= index < len(books):
        book = books[index]
        book['title'] = input(f"New title ({book['title']}): ") or book['title']
        book['author'] = input(f"New author ({book['author']}): ") or book['author']
        book['year'] = input(f"New year ({book['year']}): ") or book['year']
        book['genre'] = input(f"New genre ({book['genre']}): ") or book['genre']
        book['read'] = input("Mark as read? (yes/no): ").strip().lower() == "yes"
        save_books(books)
        print("Book updated successfully!")
    else:
        print("Invalid selection!")

def search_books(books):
    """Search for books by title, author, or genre."""
    term = input("Enter search term: ").strip().lower()
    results = [book for book in books if term in book['title'].lower() or term in book['author'].lower() or term in book['genre'].lower()]
    
    if results:
        for book in results:
            print(f"\nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\nGenre: {book['genre']}\nRead: {'Yes' if book['read'] else 'No'}")
    else:
        print("No books found!")

def display_books(books):
    """Display all books in the collection."""
    if books:
        for book in books:
            print(f"\nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\nGenre: {book['genre']}\nRead: {'Yes' if book['read'] else 'No'}")
    else:
        print("No books in the collection!")

def main():
    books = load_books()
    while True:
        print("\nBook Manager Menu")
        print("1. View Books")
        print("2. Add Book")
        print("3. Delete Book")
        print("4. Update Book")
        print("5. Search Books")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            display_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            delete_book(books)
        elif choice == "4":
            update_book(books)
        elif choice == "5":
            search_books(books)
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
