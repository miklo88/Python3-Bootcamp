class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} written by: {self.author} pages: {self.pages}'

    def __len__(self):
        return {self.pages}

    def __del__(self):
        return f"A book object has been deleted."

# title, author, pages = input('Book title: , Book Author: , Pages: ')
# print(title)
# print(title)

book = Book("Hello and Hi", "Lynda.com", 50)

print(book)
# print(len(book))
# print(str(book))
# print(len(book))
# del book
# if breaks with error 'book' was not defined. 
# print(book)
