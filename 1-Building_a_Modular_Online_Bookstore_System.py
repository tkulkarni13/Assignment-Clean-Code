from book import Book # import Book module

# Testing Book module
if __name__ == "__main__":
    book1 = Book("Harry Potter", "J. K. Rowling", 7.99, 4)
    book2 = Book("Green Eggs and Ham", "Dr. Suess", 4.99, 1)

    book1.checkout_book()
    book1.display_book_info()

    book2.checkout_book()
    book2.checkout_book() # Should notify user when 0 books are in stock
    book2.display_book_info()