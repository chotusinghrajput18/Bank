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
    def showBooks(self):
        print(self.books)
    def searchBook(self):
        book=input("enter book to search: ")
        if book in self.books:
            print("Book found")
        else:
            print("Book not found")
    def __str__(self):
        return f"Library has {len(self.books)} books"
    def __repr__(self):
        return f"Library has {len(self.books)} books"
    def __len__(self):
        return len(self.books)
    def __getitem__(self, index):
        return self.books[index]
L1=Library()
L1.addBook()