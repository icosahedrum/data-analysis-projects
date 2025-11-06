# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.
print(text[0:12])

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!
print(text[-12:])

# 3. Print a slice of the middle 12 characters from 'text'.

print(text[int(len(text)/2)-6: int(len(text)/2)-6 + 12])


# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.
for i in word[::-1]:
    print(i)

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string.
# For example, if given 'good', print 'doog' on one line.

reversal = ''

for i in word[::-1]:
    reversal += i

print(reversal)


# 3. Refactor the code to print a combination of the original and reversed string.
# For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').

reversal = ''

for i in word[::-1]:
    reversal += i

print(word+reversal)