# Exercise 1: Calculate the multiplication and sum of two numbers.
"""
Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
>>> multisum(20, 30)
600
>>> multisum(40, 30)
70
"""
"""*** YOUR CODE HERE ***"""
def multisum(a, b):
    if a * b > 1000:
        return a + b
    else:
        return a * b


# Exercise 2: Print the sum of the current number and the previous number.
"""
Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
>>> sumofprevnum(10)
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17
"""
"""*** YOUR CODE HERE ***"""
def sumofprevnum(x):
    sum = 0
    for i in range(x):
        sum += i
    return sum


# Exercise 3: Print First 10 natural numbers using while loop.
"""
>>> loopfunc(10)
1
2
3
4
5
6
7
8
9
10
"""
"""*** YOUR CODE HERE ***"""
def loopfuncx(x):
    x = 1
    while x <= 10:
        print(x)
        x += 1


# Exercise 4: Calculate the sum of all numbers from 1 to a given number.
"""
Write a program to accept a number from a user and calculate the sum of all numbers form 1 to a given number. For example, if the user entered 10 the output should be 55. (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)
>>> summation(10)
55
"""
"""*** YOUR CODE HERE ***"""
n = input("Enter a number: ")
def summation(x):
    total = 0
    # Sequence is n + (n + 1) + (n + 2) + (n + 3) + ... + (n + x)
    for i in range(x, n + 1):
        total += i
    return total


# Exercise 5: Find the factorial of a given number.
"""
Write a program to use the loop to find the factorial of a given number. The factorial (symbol: !) means to multiply all whole numbers from our chosen number down to 1.
>>> factorial(5)
120
>>> factorial(4)
24
>>> factorial(3)
6
"""
"""*** YOUR CODE HERE ***"""
def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()