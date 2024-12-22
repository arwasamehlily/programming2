# Pythonic Code
# __getitem__
from collections.abc import Sequence


class items(Sequence):
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)


obj = items(10, 20, 30)
print(len(obj))  # 3
print(obj[0])  # 10
print(obj[1])  # 20

# CONTEXT MANGERS
# with open('example.txt', 'r') as file:
# content = file.read()
# print(content)


class MyContextManager:
    def __enter__(self):
        print("Initializing resources")
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        print("Cleaning up resources")
        if exc_type:
            print(f"An exception of type {exc_type} occurred: {exc_value}")
        return False

#Comprehensions and assignment
#LISTS
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10]

#SETS
odd_numbers = {x for x in range(1, 11) if x % 2 != 0}
print(odd_numbers)  # {1, 3, 5, 7, 9}

#DICT
number_dict = {x: x * 2 for x in range(1, 6)}
print(number_dict)  # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

#Properties
class Person:
    def __init__(self, name, age):
        self._name = name  
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value
        else:
            print("Name should be longer than 3 characters")

p = Person("Lily", 19)
print(p.name)  
#p.name = "L"  

#Single Underscore
class MyClass:
    def __init__(self):
        self._name = "John"  

    def _private_method(self):
        print("This is a private method")

#Double Underscore
class MyClass2:
    def __init__(self):
        self.__secret = "This is a secret" 
obj = MyClass2()
#print(obj.__secret)

#Dataclasses
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cant be negative")

person1 = Person("Leila", 25)
person2 = Person("Ahmed", 30)

print(person1)  

#Iterator

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1


my_iter = MyIterator(0, 5)
for num in my_iter:
    print(num)
