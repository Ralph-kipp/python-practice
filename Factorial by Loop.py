# Loop until the user enters a valid integer
from numbers import Number

Number = 0
while True:
    try:
        Number = int(input("Type a number: "))
        break  # Exit loop if input is valid
    except:
        print("That is not a number. Try again.")
        continue  # Ask again if input is invalid

# Function to calculate factorial iteratively
def Factorial(Number):
    result = 1  # Initialize result to 1 (factorial of 0 and 1)
    for i in range(1, Number + 1):
        # Multiply result by current number i
        result *= i
        # Print the current step in the factorial calculation
        print(f"{i}! ({result//i} by {i}) = {result}")
    return result  # Return the final factorial value

# Call the factorial function and print the result
print(Factorial(Number))
