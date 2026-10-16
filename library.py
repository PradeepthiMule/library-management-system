books = []

def add_book(title, author):
    books.append({"title": title, "author": author})
    print(f"Book added: {title}")

def display_books():
    if not books:
        print("No books available.")
    else:
        for book in books:
            print(f"{book['title']} by {book['author']}")

add_book("Python Basics", "John Smith")
add_book("Data Structures", "Jane Doe")

print("\nLibrary Book List:")
display_books()