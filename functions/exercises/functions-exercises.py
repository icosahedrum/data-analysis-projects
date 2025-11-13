# Part 1 A -- Make a Line
def line(n: int):
    string = ""
    for i in range(n):
        string += "#"
    return string


# print(line(4))

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square

def square_of_hashes(side: int):
    square = ""
    for i in range(side):
        square += line(side)
        if i < side - 1:
            square += "\n"
    return print(square)

# square_of_hashes(5)


# Part 1 C -- Make a Rectangle

def rectangle_of_hashes(width: int, height: int):
    rectangle = ""
    for i in range(height):
        rectangle += line(width)
        if i < height - 1:
            rectangle += "\n"
    return rectangle


# print(rectangle_of_hashes(5, 3))



# Part 2 A -- Make a Stairs

def make_downward_stairs(height):
   stairs = ""
   for i in range(height):
      stairs += line(i+1)
      if i < height - 1:
         stairs += "\n"
   return stairs

# print(make_downward_stairs(5))


# Part 2 B -- Make Space-Line 

def make_space_line(blanks: int, meat: int):
    return f' ' * blanks + '#' * meat + ' ' * blanks

# print(make_space_line(3, 5))

# Part 2 C -- Make Isosceles Triangle

def make_isosceles_triangle(height):
   triangle = ""
   for i in range(height):
      triangle += make_space_line(height - i - 1, 2 * i + 1)
      if i < height - 1:
         triangle += "\n"
   return print(triangle)

# make_isosceles_triangle(5)



# Part 3 -- Make a Diamond

def make_diamond(height):
   diamond = ""

   for i in range(height):
      spaces = " " * (height - i - 1)
      hashy = "#" * (2 * i + 1)
      diamond += spaces + hashy + "\n"

   for i in range(height - 2, -1, -1):
      spaces = " " * (height - i - 1)
      hashy = "#" * (2 * i + 1)
      diamond += spaces + hashy + "\n"

   return diamond

print(make_diamond(5))



