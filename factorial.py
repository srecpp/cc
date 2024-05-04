def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Test cases
numbers = [5, 0, 3, 7]
for num in numbers:
    print("Factorial of", num, "is", factorial(num))
