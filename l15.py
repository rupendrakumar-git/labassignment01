def l15_1():
    n = int(input())
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()

def l15_2():
    start = int(input())
    end = int(input())
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total = total + i
    print(total)

def l15_3():
    start = int(input())
    end = int(input())
    divisor = int(input())
    count = 0
    for i in range(start, end + 1):
        if i % divisor == 0:
            count = count + 1
    print(count)

def l15_4():
    number = int(input())
    largest = 0
    while number > 0:
        digit = number % 10
        if digit > largest:
            largest = digit
        number = number // 10
    print(largest)

def reverse_number(n):
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    return reverse

def l15_5():
    number = int(input())
    print(reverse_number(number))

def l15_6():
    number = int(input())
    if number == reverse_number(number):
        print(True)
    else:
        print(False)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def l15_7():
    n = int(input())
    print(is_prime(n))

def l15_8():
    start = int(input())
    end = int(input())
    for n in range(start, end + 1):
        if is_prime(n):
            print(n)

def l15_9():
    n = int(input())
    while n < 0:
        n = int(input())
    fact = 1
    while n > 0:
        fact = fact * n
        n = n - 1
    print(fact)

def l15_10():
    price = float(input())
    quantity = int(input())
    discount = float(input())
    total = price * quantity
    total = total - (total * discount / 100)
    print(total)

def l15_11():
    total = 0
    count = 0
    n = float(input())
    while n != 0:
        total = total + n
        count = count + 1
        n = float(input())
    if count > 0:
        print(total / count)
    else:
        print(0)

def l15_12():
    largest = None
    n = int(input())
    while n != -1:
        if largest is None or n > largest:
            largest = n
        n = int(input())
    print(largest)

def is_multiple_of_three(n):
    return n % 3 == 0

def l15_13():
    start = int(input())
    end = int(input())
    for i in range(start, end + 1):
        if is_multiple_of_three(i):
            continue
        print(i)

def l15_14():
    start = int(input())
    end = int(input())
    target = int(input())
    found = False
    for i in range(start, end + 1):
        if i == target:
            found = True
            break
    if found:
        print("Found")
    else:
        print("Not found")

def l15_15():
    secret = int(input())
    count = 0
    while True:
        guess = int(input())
        count = count + 1
        if guess == secret:
            break
        elif guess > secret:
            print("Too high")
        else:
            print("Too low")
    print("Attempts:", count)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def l15_16():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")
        choice = input()
        if choice == "5":
            break
        a = float(input())
        b = float(input())
        if choice == "1":
            print(add(a, b))
        elif choice == "2":
            print(subtract(a, b))
        elif choice == "3":
            print(multiply(a, b))
        elif choice == "4":
            print(divide(a, b))

def l15_17():
    marks = []
    for i in range(3):
        m = float(input())
        while m < 0 or m > 100:
            m = float(input())
        marks.append(m)
    average = sum(marks) / 3
    print(average)

def l15_18():
    text = input().lower()
    vowels = 0
    consonants = 0
    for ch in text:
        if ch.isalpha():
            if ch in "aeiou":
                vowels = vowels + 1
            else:
                consonants = consonants + 1
    print(vowels, consonants)

def l15_19():
    text = input()
    seen = ""
    repeated = None
    for ch in text:
        if ch in seen:
            repeated = ch
            break
        seen = seen + ch
    if repeated is not None:
        print(repeated)
    else:
        print("No repetition")

def l15_20():
    total = 0
    n = int(input())
    while n != 0:
        if n < 0:
            n = int(input())
            continue
        total = total + n
        n = int(input())
    print(total)

def l15_21():
    name = input()
    passing_mark = int(input())
    passing = 0
    failing = 0
    score = int(input())
    while score != -1:
        if score >= passing_mark:
            passing = passing + 1
        else:
            failing = failing + 1
        score = int(input())
    print(name)
    print("Passing:", passing)
    print("Failing:", failing)

def classify(number):
    if number % 5 == 0:
        return "Multiple of 5"
    if number % 2 == 0:
        return "Even"
    return "Odd"

def l15_22():
    start = int(input())
    end = int(input())
    for i in range(start, end + 1):
        print(i, classify(i))

def l15_23():
    limit = int(input())
    total = 0
    while True:
        n = int(input())
        if n < 0:
            continue
        total = total + n
        if total > limit:
            break
    print(total)

def is_even(n):
    if n % 2 == 0:
        return True
    return False

def sum_digits(n):
    total = 0
    while n > 0:
        total = total + n % 10
        n = n // 10
    return total

def l15_24():
    n = int(input())
    if is_even(n):
        print("Even")
    else:
        print("Odd")
    if is_prime(n):
        print("Prime")
    else:
        print("Not Prime")
    print("Sum of digits:", sum_digits(n))

def l15_25():
    name = input()
    pass_mark = int(input())
    total = 0
    count = 0
    marks = int(input())
    while marks != -1:
        if marks < 0 or marks > 100:
            marks = int(input())
            continue
        total = total + marks
        count = count + 1
        marks = int(input())
    if count > 0:
        average = total / count
    else:
        average = 0
    print(name)
    print("Total:", total)
    print("Average:", average)
    if average >= pass_mark:
        print("Pass")
    else:
        print("Fail")
