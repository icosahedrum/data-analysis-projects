my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.

# result = my_string.removeprefix(my_string[:3]) + my_string[:3]
# print(result)

# Use a template literal to print the original and modified string in a descriptive phrase.

# print(f'OG String: "{my_string}" | Modified String: "{result}"')

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.

# user_input = int(input(f'Enter a number of letters to relocate: '))

# c) Add validation to your code to deal with user inputs that are longer than the word.
# In such cases, default to moving 3 characters. Also, the template literal should note the error.

# if user_input > len(my_string):
#     result = my_string.removeprefix(my_string[:3]) + my_string[:3]
# else:
#     result = my_string.removeprefix(my_string[:user_input]) + my_string[:user_input]
#
# print(result)

number_of_letters = int(input("Enter the number of letters that will be relocated:"))

if number_of_letters > len(my_string):
    print(f"Invalid input: {number_of_letters} is larger than word. Default to 3 characters.")
    result = my_string.removeprefix(my_string[:3]) + my_string[:3]
else:
    result = my_string.removeprefix(my_string[:number_of_letters]) + my_string[:number_of_letters]

print(f"The original string is {my_string} and the updated string is {result}")