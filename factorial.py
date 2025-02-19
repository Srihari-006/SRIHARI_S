n=int(input("Enter an integer :"))
def factorial_loop(n):
    result = 1
    for i in range(1, n ):
        result *= i
    return result

# Example usage
print(factorial_loop(n))
