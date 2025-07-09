>>> book=Book.objects.get(author="George Orwell")
    book.delete()
(1, {'bookshelf.Book': 1})