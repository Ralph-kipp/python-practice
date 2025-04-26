#Check if the number is even or odd

def Number_Intake():
    while True:
        try:
            Number = int(input("Enter a number to check if odd or even -> "))
            break  # Exit loop if input is valid
        except:
            print("That is not a number. Try again.")
            continue  # Keep asking until a valid integer is entered
    return Number

# Function to check if the input number is even or odd
def Reccursive_Division(Input):
    # Check remainder when divided by 2
    if (Input % 2) == 1:
        print('Odd number')
    else:
        print('Even number')

# Get the number from user
Input = Number_Intake()

# Call the function to print if the number is odd or even
Reccursive_Division(Input)
