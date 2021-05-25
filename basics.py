#FUNCTIONS

from abc import ABC, abstractmethod, abstractproperty


def add(x, y):
    return x+y # If return is skipped, the method returns a None

print(add(1,2))

print(add(x=5,y=7)) # Will print 12

def add(x, y=2):
  return x+y

print(add(5)) # Will return 7



#EXCEPTION HANDLING

try:
    assert(1==2) # This will cause an error
except AssertionError:
    print("Caught Assertion Exception")
except : # catch all exceptions
    print("Caught unknown exception")
else: # happy path
    print("No exceptions raised")
finally: # will execute regardless of exceptions or happy path
    print("Done with the assertion")



#CLASS

class Dog:
    tagf = "1"
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
Dog.tagf = "2"
print(d.tricks)
print(d.tagf)
print(e.tricks)
print(e.tagf)



class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
class Pentagon(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
class Hexagon(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")
class Quadrilateral(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")
# Driver code
R = Triangle()
R.noofsides()
K = Quadrilateral()
K.noofsides()
R = Pentagon()
R.noofsides()
K = Hexagon()
K.noofsides()



class R:
    def rk(self):
        print("Abstract Base Class")
class K(R):
    def rk(self):
        super().rk()
        print("subclass")
# Driver code
r = K()
r.rk()



class parent(ABC):
    @abstractproperty
    def geeks(self):
        return "parent class"
class child(parent):
    @property
    def geeks(self):
        return "child class"
try:
    r = parent()
    print(r.geeks)
except Exception as err:
    print(err)
r = child()
print(r.geeks)



class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Lion(Animal):
    def move(self):
        print("I can roar") 
try:
    c=Animal()
    print(c.move())
except Exception as err:
    print(err)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, 2021 - year)
       
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
   
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print (person1.age)
print (person2.age)

# print the result
print (Person.isAdult(22))



#TEXT FILE READ/WRITE

# read line by line
f = open("/tmp/foo.txt","r")
for line in f:
    print(line)
f.close()

# read the entire file in memory
f = open("/tmp/foo.txt","r")
contents = f.read()
print(contents)
f.close()

# write to a file
f = open("/tmp/bar.txt","r+") # open for both read and write
f.write("This is a test")
contents = f.read()
print(contents) # will print "This is a test"



#HTTP

import requests
r = requests.get("https://lobster1234.github.io")
print(r.headers) # headers as a dict
print(r.status_code) # 200
print(r.content) # body
r.close()

