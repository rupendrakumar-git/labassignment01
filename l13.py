def l13_1():
    n = float(input())
    if n > 0:
        print("Positive")

def l13_2():
    n = int(input())
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

def l13_3():
    age = int(input())
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible")

def l13_4():
    a = float(input())
    b = float(input())
    if a > b:
        print(a)
    else:
        print(b)

def l13_5():
    n = float(input())
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

def l13_6():
    marks = float(input())
    if marks >= 80:
        print("A")
    elif marks >= 60:
        print("B")
    else:
        print("C")

def l13_7():
    for i in range(1, 6):
        print(i)

def l13_8():
    for i in range(2, 11, 2):
        print(i)

def l13_9():
    for i in range(10, 0, -1):
        print(i)

def l13_10():
    n = int(input())
    total = 0
    for i in range(1, n + 1):
        total = total + i
    print(total)

def l13_11():
    n = int(input())
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

def l13_12():
    word = input()
    for ch in word:
        print(ch)

def l13_13():
    i = 1
    while i <= 5:
        print(i)
        i = i + 1

def l13_14():
    word = input()
    while word != "quit":
        word = input()

def l13_15():
    total = 0
    n = int(input())
    while n != 0:
        total = total + n
        n = int(input())
    print(total)

def l13_16():
    i = 10
    while i >= 1:
        print(i)
        i = i - 1
    print("Blastoff")

def l13_17():
    for i in range(1, 11):
        if i == 7:
            break
        print(i)

def l13_18():
    for i in range(1, 11):
        if i % 2 != 0:
            continue
        print(i)

def l13_19():
    for ch in "APPLE":
        if ch == "P":
            continue
        print(ch)

def l13_20():
    while True:
        password = input()
        if password == "secret":
            break

def l13_21():
    for i in range(1, 4):
        if i == 5:
            break
    else:
        print("Number not found")

def l13_22():
    i = 1
    while i <= 3:
        i = i + 1
    else:
        print("Countdown finished successfully")

def l13_23():
    text = input().lower()
    count = 0
    for ch in text:
        if ch in "aeiou":
            count = count + 1
    print(count)

def l13_24():
    n = int(input())
    fact = 1
    while n > 0:
        fact = fact * n
        n = n - 1
    print(fact)

def l13_25():
    if 10 > 5:
        pass
