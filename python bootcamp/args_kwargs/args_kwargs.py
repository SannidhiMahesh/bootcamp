#*args
#program to add all the numbers

def sum_numbers(*args):
    # Initialize the total to 0
    total = 0
    # Iterate over each number in args
    for number in args:
        # Add the number to the total
        total += number
    # Return the final total
    return total

# Taking manual input from the user
numbers = input("Enter numbers separated by spaces: ")
# Converting the input string into a list of integers
# The input string is split by spaces into a list of strings,
# then each string is converted to an integer using map and list
numbers_list = list(map(int, numbers.split()))

# Using the sum_numbers function with the unpacked list of arguments
# The * operator unpacks the list into individual arguments
result = sum_numbers(*numbers_list)

# Print the result
print(f"The sum of the numbers is: {result}")

print("--------------------------------------------------------------------------------------------------\n")

#**kwargs
#program to display the user information

def print_person_info(**kwargs):
    # Iterate over each key-value pair in kwargs
    for key, value in kwargs.items():
        # Print the key and value in a formatted string
        print(f"{key}: {value}")

# Taking manual input from the user
name = input("Enter your name: ")  # Prompt the user to enter their name
age = input("Enter your age: ")    # Prompt the user to enter their age
city = input("Enter your city: ")  # Prompt the user to enter their city

# Using the print_person_info function with keyword arguments
# The function is called with named arguments, which are passed as key-value pairs
print_person_info(name=name, age=age, city=city)
