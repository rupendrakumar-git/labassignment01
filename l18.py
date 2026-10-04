def l18_1():
    a = int(input())
    b = int(input())
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    print("Quotient:", a / b)

def l18_2():
    marks = []
    for i in range(5):
        marks.append(float(input()))
    total = sum(marks)
    percentage = total / 5
    print("Total:", total)
    print("Percentage:", percentage)

def l18_3():
    n = int(input())
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

def l18_4():
    a = float(input())
    b = float(input())
    c = float(input())
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

def l18_5():
    n = int(input())
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

def l18_6():
    n = int(input())
    fact = 1
    while n > 0:
        fact = fact * n
        n = n - 1
    print(fact)

def l18_7():
    def maximum(a, b):
        if a > b:
            return a
        return b
    a = float(input())
    b = float(input())
    print(maximum(a, b))

def l18_8():
    numbers = [10, 20, 5, 40, 15]
    print("Length:", len(numbers))
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Sum:", sum(numbers))

def l18_9():
    student = {"name": "Alice", "roll_no": 1, "marks": 90}
    for key in student:
        print(key, ":", student[key])

class Student10:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

def l18_11():
    year = int(input())
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year")

def l18_12():
    start = int(input())
    end = int(input())
    for n in range(start, end + 1):
        if n < 2:
            continue
        prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            print(n)

def l18_13():
    total = 0
    count = 0
    n = int(input())
    while n != 0:
        total = total + n
        count = count + 1
        n = int(input())
    print("Count:", count)
    print("Sum:", total)

def l18_14():
    def rectangle_area(length, breadth=10):
        return length * breadth
    length = float(input())
    print(rectangle_area(length))

def l18_15():
    numbers = [1, 2, 3, 4, 5, 6]
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    print(evens)

class Rectangle16:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)

class Person17:
    def __init__(self, name):
        self.name = name

class Student17(Person17):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

class Vehicle18:
    def display(self):
        print("This is a vehicle")

class Car18(Vehicle18):
    def display(self):
        print("This is a car")

class Bike18(Vehicle18):
    def display(self):
        print("This is a bike")

class Account19:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        self.__balance = self.__balance + amount
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
    def display(self):
        print(self.__balance)

def fibonacci20(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        c = a + b
        a = b
        b = c

def l18_21():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")
        choice = input()
        if choice == "7":
            break
        a = float(input())
        b = float(input())
        if choice == "1":
            print(a + b)
        elif choice == "2":
            print(a - b)
        elif choice == "3":
            print(a * b)
        elif choice == "4":
            if b != 0:
                print(a / b)
            else:
                print("Cannot divide by zero")
        elif choice == "5":
            if b != 0:
                print(a % b)
            else:
                print("Cannot take modulus by zero")
        elif choice == "6":
            print(a ** b)
