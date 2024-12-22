from abc import ABC, abstractmethod
#The single responsibility principle
class Adder:
    def add(self, a, b):
        return a + b

class Subtractor:
    def subtract(self, a, b):
        return a - b

class Multiplier:
    def multiply(self, a, b):
        return a * b

class Divider:
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
        
adder = Adder()
subtractor = Subtractor()
multiplier = Multiplier()
divider = Divider()


result_add = adder.add(5, 3)
result_subtract = subtractor.subtract(5, 3)
result_multiply = multiplier.multiply(5, 3)
result_divide = divider.divide(5, 0)

print(result_add)
print(result_subtract)
print(result_multiply)
print(result_divide)

#The open/closed principle

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

shapes = [Rectangle(10, 5), Circle(7), Triangle(6, 4)]
for shape in shapes:
    print(f"Area: {shape.area()}")

#Liskov Substitution Principle

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

shapes = [Square(4), Rectangle(5, 10)]

for shape in shapes:
    print(f"Area: {shape.area()}")

#Interface segregation

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass 
class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass
class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass
class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")
class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")
    def fax(self, document):
        print(f"Faxing {document}...")
    def scan(self, document):
        print(f"Scanning {document}...")

#Dependency inversion


class Notification(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

class SMSNotification(Notification):
    def send_notification(self, message):
        print(f"Sending SMS: {message}")

# High-level module
class NotificationService:
    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self, message):
        self.notification.send_notification(message)

sms = SMSNotification()
service = NotificationService(sms)
service.send("Hello!")

