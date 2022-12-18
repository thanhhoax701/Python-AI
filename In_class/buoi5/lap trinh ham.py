# Pure Function #
def phep_cong(a, b):
    return a + b
print phepcong(10, 5)

# Anonymous Function #
f = lambda a, b : a * b
print f(2,3)

# Recursive function #
def factorial(n):
    if n==0:
        return 1
        return n * factorial(n-1)
    
print(factorial(5))

# First-Class function #
def f(function, *arguments):
    return function(*arguments)

print (f(max, 1, 2, 4, 7, 10, 20))
print (f(min, 1, 2, 4, 7, 10, 20))
