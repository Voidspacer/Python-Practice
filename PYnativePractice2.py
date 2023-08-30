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
def calculation(a, b):
    """
    >>> calculation(40, 10)
    50, 30
    """
    # Your code
    addition = a + b
    subtraction = a - b
    result = addition, subtraction
    return result


# Exercise 3: Create a function with a default argument.
"""
Write a program to create a function show_employee() using the following conditions:
- It should accept the employee's name and salary and display both.
- If the salary is missing in the function call then assign default value 9000 to salary.
"""
"""*** YOUR CODE HERE ***"""
bsalary = 12000
def show_employee(name1, salary):
    salary = 9000
    if name1 == 'Ben':
        return(bsalary)
    else:
        return(salary)


# Exercise 4: Create an inner function to calculate the addition in the following way
"""
- Create an outer function that will accept two parameters, a and b.
- Create an inner function inside an outer function that will calculate the addition of a and b.
- At last, an outer function will add 5 into addition and return it.
"""
"""*** YOUR CODE HERE ***"""
def calcuator(a, b):
    def calculation1(a, b):
        return a + b
    summ = calculation1(a, b)
    return summ + 5
result = calcuator(5, 10)
print(result)


if __name__ == "__main__":
    import doctest
    doctest.testmod()