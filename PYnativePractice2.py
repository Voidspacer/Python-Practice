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


# Exercise 2: Create a function with variable length of arguments.
"""
Write a program to create function func1() to accept a variable length of arguments and print their value.
"""
"""***  YOUR CODE HERE ***"""
def func1(*args):
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()