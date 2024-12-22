# Preconditions

from abc import ABC, abstractmethod


def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return a + b


a = add_numbers(4, 7)
print(a)

# Postconditions


def add_numbers(a, b):
    result = a + b
    if result < max(a, b):
        raise ValueError("Postcondition failed: result should be >= max input")
    return result


a = add_numbers(4, 7)
print(a)

# Invariants


def manipulate_list(lst):
    """
    Invariant: The length of lst should remain constant.
    """

# Side Effects


def update_database(data):
    """
    Side Effect: Updates the database with the new data.
    """


# Error handling
try:
    file = open('somefile.txt', 'r')
    content = file.read()
except FileNotFoundError:

    print("File isnt here")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cant divde by Zero")


# try:
   # with open('nofile.txt', 'r') as file:
 #       content = file.read()
# except FileNotFoundError as original_exception:
 #   raise RuntimeError("Failed to open the file for reading") from original_exception

# When inheritance is a good decision


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Bark"
    
dog = Dog()
print(dog.make_sound())
