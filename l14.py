def l14_1():
    print("Welcome to Python Programming")

def l14_2():
    name = input()
    print("Hello", name)

def l14_3():
    a = float(input())
    b = float(input())
    print(a + b)

def l14_4():
    name = input()
    age = input()
    course = input()
    print(name, age, course)

def l14_5():
    n = float(input())
    print(n ** 2)

def l14_6():
    n = int(input())
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

def l14_7():
    for i in range(1, 11):
        print(i)

def l14_8():
    n = int(input())
    for i in range(1, 11):
        print(n * i)

def l14_9():
    n = int(input())
    total = 0
    for i in range(1, n + 1):
        total = total + i
    print(total)

def l14_10():
    text = input()
    count = 0
    for ch in text:
        count = count + 1
    print(count)

def l14_11():
    text = input().lower()
    count = 0
    for ch in text:
        if ch in "aeiou":
            count = count + 1
    print(count)

def l14_12():
    n = int(input())
    fact = 1
    while n > 0:
        fact = fact * n
        n = n - 1
    print(fact)

def l14_13():
    n = int(input())
    while n > 0:
        print(n)
        n = n - 1
    print("Blastoff!")

def l14_14():
    word = input()
    while word != "quit":
        word = input()

def l14_15():
    total = 0
    n = int(input())
    while n != 0:
        total = total + n
        n = int(input())
    print(total)

def l14_16():
    for i in range(1, 21):
        if i == 12:
            break
        print(i)

def l14_17():
    target = int(input())
    for i in range(1, 11):
        if i == target:
            print("Found")
            break
    else:
        print("Not found")

def l14_18():
    for i in range(1, 21):
        if i % 2 != 0:
            continue
        print(i)

def l14_19():
    skip = int(input())
    for i in range(1, 11):
        if i == skip:
            continue
        print(i)

def l14_20():
    start = int(input())
    end = int(input())
    for i in range(start, end + 1):
        print(i)

def l14_21():
    m1 = float(input())
    m2 = float(input())
    m3 = float(input())
    total = m1 + m2 + m3
    print(total)

def l14_22():
    a = float(input())
    b = float(input())
    c = float(input())
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

def l14_23():
    while True:
        password = input()
        if password == "secret":
            break

def l14_24():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Quit")
        choice = input()
        if choice == "3":
            break

def l14_25():
    start = int(input())
    end = int(input())
    skip = int(input())
    for i in range(start, end + 1):
        if i == 50:
            break
        if i == skip:
            continue
        print(i)
