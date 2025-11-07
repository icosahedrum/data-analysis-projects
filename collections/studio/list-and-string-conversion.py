proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;)
# or just spaces.

# for string in strings:
#     if ';' in string:
#         print("semicolons:" + string)
#     elif ',' in string:
#         print("commas: " + string)
#     elif ' ' in string:
#         print('spaces: ' + string)

# b) If the string uses commas to separate the words, split it into an array, reverse the entries,
# and then join the array into a new comma separated string.

for string in strings:
    if ',' in string:
        result = ','.join(entries.strip() for entries in string.split(',')[::-1])
        print(result)

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries,
# and then join the array into a new comma separated string.

for string in strings:
    if ';' in string:
        parts = [entry.strip() for entry in string.split(';')]
        alphabetical = sorted(parts)
        result = ','.join(alphabetical)
        print(result)

# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries,
# and then join the array into a new space separated string.

for string in strings:
    if ' ' in string:
        parts = [entry.strip() for entry in string.split(' ')]
        alphabetical = sorted(parts, reverse=True)
        result = ' '.join(alphabetical)
        print(result)


# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”,
# making sure that the extra spaces are NOT part of the final string.

for string in strings:
    if ', ' in string:
        result = ','.join(entries.strip() for entries in string.split(', ')[::-1])
        print(result)