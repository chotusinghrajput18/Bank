class Library:
    def __init__(self):
        self.books = []
    def addBook(self):
        book=input("enter book to add: ")
        if book not in self.books:
            self.books.append(book)
        else:
            print("Book already exists")
    def removeBook(self):
        book=input("enter book to remove: ")
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book not found") 