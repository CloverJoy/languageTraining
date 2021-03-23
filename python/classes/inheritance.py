# main
from abc import ABC, abstractmethod


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")
# sub


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        # super() or overriden
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


class Person():
    def greet(self):
        print("Person Greet")


class Manager(Person):
    pass


manager = Manager()
manager.greet()

# pass if dont have any expression
m = Mammal()
print(isinstance(m, object))
# every class inherited from object
print(issubclass(Mammal, Animal))
print(m.age, m.weight)


class InvalidOperationError(Exception):
    pass

# best practice inheritance

# gak bisa di instantiate. abstract


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open!")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed!")
        self.opened = False

    # if class doest have this method, it becomes abstract
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class Memorystream(Stream):
    def read(self):
        print("Reading from memory stream")


stream = Memorystream()
stream.open()
