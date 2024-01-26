def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
    
# print(factorial(6))
# print(factorial(10))
# print(factorial(0))

def fibonacci (n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(6))
def countdown(n):
    while n > 0:
        print(n)
        n = n -1
    print("Blastoff")

countdown(10)