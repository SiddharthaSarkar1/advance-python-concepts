# docstring (documentation string) in Python is a string literal written as the very first statement inside a module, function, class, or method definition. Its primary purpose is to explain what the code does, and unlike regular comments, it is retained at runtime so developers can access it dynamically.

def myexpo(num1, num2):
    """ 
    This function takes one number to the power of another number and returns the result. 
    
    :param num1: this is the base
    :param num2: this is the exp    
    :return: the result of the calculation
    """
    return num1 ** num2

print(myexpo(3, 2))

print(help(myexpo))

print(myexpo.__doc__)