# Python Functions Practice
# Topics: maximum, minimum, palindrome, prime number, factorial, fibonacci


def find_maximum(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


def find_minimum(numbers):
    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

    return minimum


def is_palindrome(word):
    reversed_word = ""

    for char in word:
        reversed_word = char + reversed_word

    if word == reversed_word:
        return True
    else:
        return False


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


def fibonacci(n):
    series = []

    a = 0
    b = 1

    for i in range(n):
        series.append(a)

        next_number = a + b
        a = b
        b = next_number

    return series


# Testing all functions

numbers = [10, 45, 23, 89, 12]

print("Numbers:", numbers)
print("Maximum:", find_maximum(numbers))
print("Minimum:", find_minimum(numbers))

word = "madam"
print("Word:", word)
print("Palindrome:", is_palindrome(word))

num = 29
print("Number:", num)
print("Prime:", is_prime(num))

fact_num = 5
print("Factorial of", fact_num, ":", factorial(fact_num))

fib_count = 8
print("First", fib_count, "Fibonacci numbers:", fibonacci(fib_count))