# Book class which defines an object with a title, author, price, and stock amount
class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
    
    # Getters and Setters

    def get_title(self):
        return self.title
    
    def set_title(self, new_title):
        self.title = new_title

    def get_author(self):
        return self.author
    
    def set_author(self, new_author):
        self.author = new_author

    def get_price(self):
        return self.price
    
    def set_price(self, new_price):
        self.price = new_price

    # Availability of a book is equivalent to stock
    def get_availability(self):
        return f"{self.stock} books left in stock."
    
    def set_stock(self, new_stock):
        self.stock = new_stock

    # Decrease stock by 1 when a book is checkedout
    def checkout_book(self):
        if (self.stock) < 1:
            print("No available stock.")
        else:
            self.stock -= 1
    
    # Increment stock by 1 when a book is returned to library
    def checkin_book(self):
        self.stock  += 1
    
    # Function to display all information about this book
    def display_book_info(self):
        print(f"{self.title} by {self.author}: ${self.price} - {self.get_availability()}")