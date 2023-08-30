# Exercise 1: Create a function in Python.
"""
Write a program to create a function that takes two arguments, name and age, and print their value.
"""
"""*** YOUR CODE HERE ***"""
def information():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print("Welcome " + name + ", age " + age + "!")
information()


# Exercise 2: Return multiple values from a function.
"""
Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
"""
"""*** YOUR CODE HERE ***"""
def calculation(a, b):
    # Your code
    return a + b, a - b
res = calculation(40, 10)
print(res)