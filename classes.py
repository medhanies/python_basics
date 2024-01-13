class Person():

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def greet(self):
        return 'Hello ' + self.name.title() + ' from ' + self.address + '.'

person1 = Person('mike', '123 Bakers St')

# print(person1.greet())

class Dog():

    species = 'mammal'

    def __init__(self, breed, name, spots) -> None:
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self, number):
        return f'my dog {self.name} barks {number} times a day'


mydog = Dog('mutt', 'billy', False)

# print(mydog)

# print(mydog.breed)
# print(mydog.name)
# print(mydog.spots)
# print(mydog.species)
# print(mydog.bark(100))

class Circle():

    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius*radius*self.pi

    def get_circumference(self):
        return self.radius * Circle.pi * 2


mycircle = Circle(3)

# print(mycircle.pi)
# print(mycircle.get_circumference())
# print(mycircle.area)

'''Inheritance'''

class Animal():

    def __init__(self) -> None:
        print("Animal Created")

    def who(self):
        print("I am an Animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self) -> None:
        Animal.__init__(self)
        print('Dog Created')

bill = Dog()

bill.who()
bill.eat()