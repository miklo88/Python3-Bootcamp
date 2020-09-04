# class Book():
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f'{self.title} written by: {self.author} pages: {self.pages}'

#     def __len__(self):
#         return {self.pages}

#     def __del__(self):
#         return f"A book object has been deleted."

# # title, author, pages = input('Book title: , Book Author: , Pages: ')
# # print(title)
# # print(title)
# color = ""
# number = 0
# car = input("string:'' num: ")
# print(car)
# book = Book("Hello and Hi", "Lynda.com", 50)

# print(book)
# print(len(book))
# print(str(book))
# print(len(book))
# del book
# if breaks with error 'book' was not defined. 
# print(book)

# circles class
class Line:
    def __init__(self, coord1, coord2):
        #using tuples as attributes
        self.coord1 = coord1
        self.coord2 = coord2

    def __repr__(self):
        return f' repr return - {self.coord1} : {self.coord2}'
#  circles circumference/distance dundr method
    def distance(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2

        coord = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        return f'distance/circumference func: {coord}'
        
    #  circles slope dundr method
    def slope(self):

        x1,y1 = self.coord1
        x2,y2 = self.coord2
        slippery = (y2-y1) / (x2-x1)        
        return f'slope func: {slippery}'
        #tuples type()
coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li)
print(li.distance())
print(li.slope())

# a = input('nummies : ')
# print(a)
class Cylinder:
    def __init_f_(self, height=1, radius=1):
        #cylinder attributes
        self.height = height
        self.radius = radius
    
    def volume(self):
        pi = 3.14159
        pie = height * pi * radius ** 2
        return f'Nomnom pie: {pie}'

# Surface Area of a Cylinder = 2πr² + 2πrh
    def surface_area(self):
        pi = 3.14159
        surface_covering = 2*pi*(radius**2) + 2*pi*radius*height
        return f'just scratching the surface {surface_covering}'
        
height = 3
radius = 2
c = Cylinder()

print(c)
print(c.volume())
print(c.surface_area())

