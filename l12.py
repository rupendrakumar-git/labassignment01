def l12_1():
    year = int(input())
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year")

def l12_2():
    a = float(input())
    b = float(input())
    c = float(input())
    if a + b > c and a + c > b and b + c > a:
        print("Valid triangle")
    else:
        print("Invalid triangle")

def l12_3():
    a = float(input())
    b = float(input())
    c = float(input())
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

def l12_4():
    x = float(input())
    y = float(input())
    if x == 0 and y == 0:
        print("Origin")
    elif x == 0:
        print("Y-axis")
    elif y == 0:
        print("X-axis")
    elif x > 0 and y > 0:
        print("Quadrant I")
    elif x < 0 and y > 0:
        print("Quadrant II")
    elif x < 0 and y < 0:
        print("Quadrant III")
    else:
        print("Quadrant IV")

def l12_5():
    ch = input().lower()
    if ch in "aeiou":
        print("Vowel")
    else:
        print("Consonant")

def l12_6():
    marks = float(input())
    attendance = float(input())
    if marks >= 40 and attendance >= 75:
        print("Pass")
    elif marks < 40:
        print("Fail due to marks")
    else:
        print("Fail due to attendance")

def l12_7():
    n = int(input())
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total = total + i * i
    print(total)

def l12_8():
    n = int(input())
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    print(reverse)

def l12_9():
    n = int(input())
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

def l12_10():
    n = int(input())
    if n < 0:
        print("Invalid")
    else:
        fact = 1
        while n > 0:
            fact = fact * n
            n = n - 1
        print(fact)

def l12_11():
    n = int(input())
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()

def l12_12():
    a = int(input())
    b = int(input())
    while b != 0:
        temp = b
        b = a % b
        a = temp
    print(a)

def l12_13():
    total = 0
    n = int(input())
    while n != 0:
        total = total + n
        n = int(input())
    print(total)

def l12_14():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def l12_15():
    for i in range(1, 31):
        if i % 4 == 0 or i % 7 == 0:
            continue
        print(i)

def l12_16():
    n = 101
    while True:
        if n % 7 == 0 and n % 13 == 0:
            print(n)
            break
        n = n + 1

def l12_17():
    count = 0
    while count < 3:
        password = input()
        if password == "secret":
            break
        count = count + 1
    else:
        print("Locked")

def l12_18():
    n = int(input())
    if n < 2:
        print("Not prime")
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")

def l12_19():
    target = int(input())
    i = 1
    while i <= 10:
        if i == target:
            print("Found")
            break
        i = i + 1
    else:
        print("Target not found")

def l12_20():
    text = input()
    upper = 0
    lower = 0
    digits = 0
    for ch in text:
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
            lower = lower + 1
        elif ch.isdigit():
            digits = digits + 1
    print(upper, lower, digits)

def l12_21():
    n = int(input())
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    if original == reverse:
        print("Palindrome")
    else:
        print("Not a palindrome")

def l12_22():
    n = int(input())
    original = n
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit ** 3
        n = n // 10
    if total == original:
        print("Armstrong")
    else:
        print("Not Armstrong")

def l12_23():
    n = int(input())
    while n > 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(n)

def l12_24():
    n = int(input())
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total = total + i
    if total == n:
        print("Perfect number")
    else:
        print("Not a perfect number")

def l12_25():
    numbers = []
    n = int(input())
    while n != 0:
        numbers.append(n)
        n = int(input())
    if len(numbers) < 2:
        print("Not enough numbers")
    else:
        numbers.sort()
        print(numbers[-2])
