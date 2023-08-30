# Question 1: Return the Sum of Two Numbers
def addition(a, b):
    """
    We want to create a function that takes two numbers as arguments and returns their sum.
    >>> addition(3, 2)
    5
    >>> addition(-3, -6)
    -9
    >>> addition(7, 3)
    10
    """
    """*** YOUR CODE HERE ***"""
    return a + b


# Question 2: Return a String as an Integer
def string_int(x):
    """
    We want to create a function that takes a string and returns it as an integer.
    >>> string_int("6")
    6
    >>> string_int("1000")
    1000
    >>> string_int("12")
    12
    """
    """*** YOUR CODE HERE ***"""
    return int(x)


# Question 3: Convert Hours into Seconds
def how_many_seconds(n):
    """
    We want to write a function that converst hours into seconds.
    >>> how_many_seconds(2)
    7200
    >>> how_many_seconds(10)
    36000
    >>> how_many_seconds(24)
    86400
    """
    """*** YOUR CODE HERE ***"""
    return n * 3600


# Question 4: Maximum Edge of a Triangle
def next_edge(side1, side2):
    """
    We want to create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.
    >>> next_edge(8, 10)
    17
    >>> next_edge(5, 7)
    11
    >>> next_edge(9, 2)
    10
    """
    """*** YOUR CODE HERE ***"""
    return (side1 + side2) - 1
if __name__ == "__main__":
    import doctest
    doctest.testmod()
