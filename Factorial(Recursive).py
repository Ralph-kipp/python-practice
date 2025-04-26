def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Calculate and print the factorial of the entered number
print(f"The factorial of {number} is {factorial(number)}")
