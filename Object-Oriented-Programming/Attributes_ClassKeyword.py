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

my_dog = Dog(name='Kevin',breed='Lab',gender='M',spots=False)

print(my_dog.name)
print(my_dog.breed)
print(my_dog.gender)
print(my_dog.spots)

#an instance of the sample class
# my_sample = Sample()
# print(type(my_sample))