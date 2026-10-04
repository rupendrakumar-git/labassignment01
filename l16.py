class Student1:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print(self.name, self.roll_no, self.marks)

class Rectangle2:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def display(self):
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())

class BankAccount3:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        self.balance = self.balance - amount
    def display(self):
        print(self.balance)

class Employee4:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    def display(self):
        print(self.name, self.emp_id, self.salary)

class Book5:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        print(self.title, self.author, self.price)

class Car6:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display(self):
        print(self.brand, self.model)

class Circle7:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class Student8:
    college_name = "ABC College"
    def __init__(self, name):
        self.name = name

class Account9:
    def __init__(self, balance=0):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance = self.__balance + amount
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
    def display(self):
        print(self.__balance)

class Person10:
    def __init__(self, age=0):
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age

class Animal11:
    def sound(self):
        print("Some sound")

class Dog11(Animal11):
    def sound(self):
        print("Bark")

class Grandparent12:
    def grandparent_method(self):
        print("Grandparent method")

class Parent12(Grandparent12):
    def parent_method(self):
        print("Parent method")

class Child12(Parent12):
    def child_method(self):
        print("Child method")

class Shape13:
    def area(self):
        pass

class Circle13(Shape13):
    def area(self):
        return 3.14 * 2 * 2

class Rectangle13(Shape13):
    def area(self):
        return 4 * 5

class Vehicle14:
    def start(self):
        print("Vehicle started")

class Bike14(Vehicle14):
    def start(self):
        print("Bike started")

class Person15:
    def __init__(self, name):
        self.name = name

class Student15(Person15):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

class Dog16:
    def speak(self):
        print("Bark")

class Cat16:
    def speak(self):
        print("Meow")

class Point17:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point17(self.x + other.x, self.y + other.y)

def display_area18(shape):
    print(shape.area())

from abc import ABC, abstractmethod

class Shape19(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle19(Shape19):
    def area(self):
        return 3.14 * 1 * 1

class Rectangle19(Shape19):
    def area(self):
        return 2 * 3

class Payment20(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment20(Payment20):
    def pay(self):
        print("Paid by credit card")

class UPIPayment20(Payment20):
    def pay(self):
        print("Paid by UPI")

def squares21(n):
    for i in range(1, n + 1):
        yield i * i

def evens22(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

def use_iterator23():
    numbers = [1, 2, 3, 4, 5]
    it = iter(numbers)
    for i in range(5):
        print(next(it))

class Iterator24:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current = self.current + 1
        return value

def fibonacci25(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        c = a + b
        a = b
        b = c
