# Get input string from the user
String = input("Type in input -> ")

# Initialize an empty string to hold the reversed result
Reversed_string = ""

# Get the length of the input string
target_value = len(String)

# Recursive function to reverse the string
def String_reversal(Reversed_string, target_value):
    # Base case: if target_value is 0, return the reversed string so far
    if target_value == 0:
        return Reversed_string
    else:
        # Add the character at position target_value-1 to the reversed string
        Reversed_string += String[target_value - 1]
        # Recursively call the function with target_value decreased by 1
        return String_reversal(Reversed_string, target_value - 1)

# Call the recursive function and print the reversed string
print(String_reversal(Reversed_string, target_value))
