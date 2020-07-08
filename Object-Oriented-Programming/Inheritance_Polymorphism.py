'''
INHERITANCE - A way to use classes when classes have already been defined
extra sugar
POLYMORPHISM - Different object classes can reference the same method name. Those methods can be called from a variety of places where a 
bunch of different objects can be passed in.
'''

# class Animal():

#     def __init__(self):
#         print("ANIMAL CREATED")

#     def who_am_i(self):
#         print("I am animal")

#     def eat(self):
#         print("I am eating")

# #created a Dog class which inherits Animal traits!
# class Dog(Animal):

#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog Created")

#     #overwriting an older method
#     def who_am_i(self):
#         print("I am a dog!")

#     def eat(self):
#         print("I am hungry dog")
    
#     def bark(self):
#         print("Woof woof!")

# mydog = Dog()
# mydog.who_am_i()
# mydog.eat()
# mydog.bark()
# # myanimal = Animal()

# # print(myanimal)
# # myanimal.speak()
#############################
# #POLYMORPHISM - quick skinny
# class Dog():
#     def __init__(self,name):
#         self.name = name
    
#     def speak(self):
#         return self.name + " says woof"

# class Cat():
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         return self.name + " says meow"

# niko = Dog("niko")
# felix = Cat("felix")
# print(niko.speak())
# print(felix.speak())

# #iterating polymorphism example
# for pet in [niko,felix]:
#     print(pet)
#     print(pet.speak())
# #function polymorphism example
# def pet_speak(pet):
#     print(pet.speak())
#     #invoking
# pet_speak(niko)
# pet_speak(felix)
#abstract class - one that never expects to be instantiated. designed to only serve as a base class
class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method.")

class Dog(Animal):
    def speak(self):
        return self.name+ " says woof"
class Cat(Animal):
    def speak(self):
        return self.name+ " says somethin sassy"

fido = Dog('Fido')
diesel = Cat('Diesel')
print(fido.speak())
print(diesel.speak())