def l17_1():
    square = lambda x: x * x
    n = int(input())
    print(square(n))

def l17_2():
    larger = lambda a, b: a if a > b else b
    a = int(input())
    b = int(input())
    print(larger(a, b))

def l17_3():
    students = [("Alice", 70), ("Bob", 90), ("Charlie", 80)]
    students.sort(key=lambda s: s[1])
    print(students)

def l17_4():
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x * x, numbers))
    print(squares)

def l17_5():
    celsius = [0, 10, 20, 30]
    fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celsius))
    print(fahrenheit)

def l17_6():
    numbers = [1, 2, 3, 4, 5, 6]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(evens)

def l17_7():
    numbers = [-3, -1, 0, 1, 2]
    positives = list(filter(lambda x: x > 0, numbers))
    print(positives)

def l17_8():
    students = [("Alice", 70), ("Bob", 50), ("Charlie", 80)]
    passed = list(filter(lambda s: s[1] >= 60, students))
    print(passed)

def l17_9():
    numbers = [1, 2, 3, 4, 5, 6]
    evens = filter(lambda x: x % 2 == 0, numbers)
    squares = list(map(lambda x: x * x, evens))
    print(squares)

def l17_10():
    from functools import reduce
    numbers = [1, 2, 3, 4]
    product = reduce(lambda a, b: a * b, numbers)
    print(product)

class Calculator11:
    add = lambda self, a, b: a + b
    multiply = lambda self, a, b: a * b

class Engine12:
    def __init__(self, engine_type):
        self.engine_type = engine_type

class Car12:
    def __init__(self, engine):
        self.engine = engine

class Temperature13:
    def __init__(self):
        self.__celsius = 0
    @property
    def celsius(self):
        return self.__celsius
    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self.__celsius = value

class Employee14:
    def display_role(self):
        pass

class Manager14(Employee14):
    def display_role(self):
        print("Manager")

class Developer14(Employee14):
    def display_role(self):
        print("Developer")

class Employee15:
    def calculate_salary(self):
        return 0

class Manager15(Employee15):
    def calculate_salary(self):
        return 50000

class Developer15(Employee15):
    def calculate_salary(self):
        return 60000

class Printer16:
    def display(self):
        print("Printing")

class Screen16:
    def display(self):
        print("Displaying")

def show16(obj):
    obj.display()

class Reverse17:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index = self.index - 1
        return value

def primes18(limit):
    for n in range(2, limit + 1):
        prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            yield n

def words19(sentence):
    for word in sentence.split():
        yield word
