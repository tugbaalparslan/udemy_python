from pip._vendor.html5lib._utils import memoize


# Write a Python program of recursive function of sum of a list with inner lists.
def recursive_inner_list_sum(data_list):
    total = 0
    for element in data_list:
        if isinstance(element, list):
            total += recursive_inner_list_sum(element)
        else:
            total += element

    return total


print("Recursive inner list:", recursive_inner_list_sum([1, 2, [3, 4], [5, 6]]))


# Write a Python program to calculate the sum of a list of numbers.
def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])


print("List sum is:", list_sum([2, 4, 5, 6, 7]))


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci:", fibonacci(6))


def get_sum_of_digits(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + get_sum_of_digits(num_list[1:])


def sum_of_digits(num):
    num_list = []
    for x in str(num):
        num_list.append(int(x))
    print(num_list)
    return get_sum_of_digits(num_list)


print("Sum of digits:", sum_of_digits(123))


def sumDigits(n):
    # if n == 0:
    #     return 0
    # else:
    #     return n % 10 + sumDigits(n // 10)

    # sum = 0
    # while n > 0:
    #     sum += n % 10
    #     n = n//10

    return sum


print("Sum of Digits:", sumDigits(345))
print("Sum of Digits:", sumDigits(45))


def sum_of_smaller_even_nums(n):
    if n < 1:
        return 0
    else:
        return n + sum_of_smaller_even_nums(n - 2)


print("Sum of smaller even nums:", sum_of_smaller_even_nums(10))


# Write a Python program to calculate the value of 'a' to the power 'b'. (power(3,4) -> 81
def power_of(a, b):
    if b == 0:
        return 1
    else:
        return a * power_of(a, b - 1)


print("Power of:", power_of(3, 4))


# The Tribonacci sequence Tn is defined as follows: T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

@memoize
def tribonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


print("Tribonacci:", tribonacci(25))


# Write a Python program to find the greatest common divisor (gcd) of two integers.
def Recurgcd(a, b):
    low = min(a, b)
    high = max(a, b)

    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return Recurgcd(low, high % low)


print("Greatest common divisor is:", Recurgcd(12, 14))
