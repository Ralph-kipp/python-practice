#Sum of all the elements in a list
# from curses.ascii import isdigit

print("How many values? ->")
Total_Count = int(input())  # Get the total number of values to sum

List_of_Numbers = []  # Initialize empty list to hold numbers

# Collect the numbers from user input
while len(List_of_Numbers) < Total_Count:
    print(f"Enter number {len(List_of_Numbers) + 1} to sum -> ")
    Number = input("")
    try:
        List_of_Numbers.append(int(Number))  # Convert input to int and add to list
    except:
        print(f"'{Number}' is not a number. Try again.")  # Handle invalid input
        continue

i = 0  # Start index for recursion
Total = 0  # Initialize total sum

# Recursive function to sum the list elements
def Summation(List_of_Numbers, Total, i):
    # Base case: if index reaches the count, stop recursion
    if i < Total_Count:
        Total += List_of_Numbers[i]  # Add current element to total
        print(f"{Total}")  # Print running total
        i += 1  # Move to next element
        Summation(List_of_Numbers, Total, i)  # Recursive call

# Call the recursive summation function
Summation(List_of_Numbers, Total, i)
