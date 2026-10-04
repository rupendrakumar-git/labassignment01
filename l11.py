def l11_1():
    print("Hello, World!")

def l11_2():
    name = "Your Name"
    print(name)

def l11_3():
    age = 20
    print(age)

def l11_4():
    a = 15
    b = 25
    print(a + b)

def l11_5():
    a = 50
    b = 18
    print(a - b)

def l11_6():
    a = 12
    b = 8
    print(a * b)

def l11_7():
    a = 100
    b = 4
    print(a / b)

def l11_8():
    a = 27
    b = 5
    print(a % b)

def l11_9():
    a = 27
    b = 5
    print(a // b)

def l11_10():
    a = 9
    print(a ** 2)

def l11_11():
    name = input()
    print("Hello", name)

def l11_12():
    n = int(input())
    print(n)

def l11_13():
    a = int(input())
    b = int(input())
    print(a + b)

def l11_14():
    length = float(input())
    breadth = float(input())
    print(length * breadth)

def l11_15():
    length = float(input())
    breadth = float(input())
    print(2 * (length + breadth))

def l11_16():
    radius = float(input())
    print(3.14 * radius * radius)

def l11_17():
    celsius = float(input())
    fahrenheit = (celsius * 9 / 5) + 32
    print(fahrenheit)

def l11_18():
    p = float(input())
    r = float(input())
    t = float(input())
    si = (p * r * t) / 100
    print(si)

def l11_19():
    a = float(input())
    b = float(input())
    c = float(input())
    print((a + b + c) / 3)

def l11_20():
    a = input()
    b = input()
    print("Before:", a, b)
    temp = a
    a = b
    b = temp
    print("After:", a, b)

def l11_21():
    m1 = float(input())
    m2 = float(input())
    m3 = float(input())
    m4 = float(input())
    m5 = float(input())
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5
    print(total, percentage)

def l11_22():
    salary = float(input())
    deduction = float(input())
    print(salary - deduction)

def l11_23():
    p1 = float(input())
    p2 = float(input())
    p3 = float(input())
    print(p1 + p2 + p3)

def l11_24():
    price = float(input())
    discount = float(input())
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    print(discount_amount, final_price)

def l11_25():
    distance = float(input())
    mileage = float(input())
    fuel_price = float(input())
    fuel_used = distance / mileage
    cost = fuel_used * fuel_price
    print(fuel_used, cost)
