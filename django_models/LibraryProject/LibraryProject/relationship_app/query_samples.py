from models import *

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name: {author_name}")

# Query all books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Assuming a ManyToManyField from Library to Book
        print(f"Books in {library_name} library:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")

#Retrieve the librarian for a library
def get_librarian_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian.first()
        if librarian:
            print(f'Librarian for {library_name} is: {librarian}')
        else:
            print(f'No librarian for {library_name} library')
        
    except Library.DoesNotExist:
        print(f"The library, {library_name} does not exist")

# Example usage
if __name__ == "__main__":
    get_books_by_author("J.K. Rowling")
    get_books_in_library("Central Library")
    get_librarian_in_library("Central Library")