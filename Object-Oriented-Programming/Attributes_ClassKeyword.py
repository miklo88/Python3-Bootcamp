'''
Object Oriented Programming (OOP) 
allows programmers to create their on objects that have methods and attributes.
Recall that after defining a string, list, dictionary, or other objects, 
you were able to call methods off them with the .method_name() syntax.

These methods act as functions that use information about the object, as well as the 
object itself to return results, or change the current object.

For example this includes appending to a list, or counting the occurnces of an element in a tuple.
'''
#this is the class keyword, the name of the class.
class NameOfClass():
#method inside a class call. instance of the actual object. 
    def __init__(self,param1,param2):
        #param1 and param2 are keywords python expects you to pass
        self.param1 = param1
        #this lets python know that you are referring to self.param1
        self.param2 = param2
    #self.param2 = param2 actually links it up to the object.

    #self as a param connects the methods in this class. so it connects the method above.
    def some_method(self):
        #perform some action
        print(self.param1)
    
### PART ONE
# creating our own user defined object
# since everything in python is an object.
class Dog():
#PT 2 Class object attribute
#same for any instance of a class
    species = 'mammal'

#your params are attributes of your object
    def __init__(self,name,breed,gender,spots):
        #Attributes
        #we take in the argument
        #assign it using self.attribute_name
        self.name = name
        self.breed = breed
        self.gender =  gender
        #boolean true/false
        self.spots = spots

        #methods = operations/actions ---> methods
    # def bark(self):
    def bark(self,number):
        # print('GURRRL')
        print('GURRRL My name is {} and the number is {}'.format(self.name,number))

my_dog = Dog(name='Kevin',breed='Lab',gender='M',spots=False)

print(my_dog.name)
print(my_dog.breed)
print(my_dog.gender)
print(my_dog.spots)
# the class object attribute
print(my_dog.species)

# print(my_dog.bark())
print(my_dog.bark(5))

####NEW CLASS
class Circle():
#CLASS OBJECT ATTRIBUTE
    pi = 3.14
#radius has a default value given to it that can be overridden
    def __init__(self,radius=1):
        self.radius = radius
        #at the end circle.pi is done because its a reference to the class object. easier to read for bigger classes.
        # self.area = radius*radius*Circle.pi 
        self.area = radius*radius*self.pi
    #METHOD
    def get_circumference(self):
        #note there is the cirlce.pi reference again.
        # return self.radius * Cirlce.pi * 2
        return self.radius * self.pi * 2

# my_circle = Circle()
#radius value overridden
my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)
print(my_circle.get_circumference())



#an instance of the sample class
# my_sample = Sample()
# print(type(my_sample))

###PART TWO
#class object attributes, then methods
