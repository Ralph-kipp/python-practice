# Function to find the sum of digits
def sum_of_digits(n):
    if n == 0:
        return 0  # If number is 0, stop and return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)  # Add last digit and call function on remaining number

# Example usage
number = int(input("Enter a number: "))  # Ask user for a number
print(f"The sum of digits of {number} is {sum_of_digits(number)}")
