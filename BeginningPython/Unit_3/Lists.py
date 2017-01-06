"""
Python knows a number of compound data types, used to group together other values. the most versatile
is the list, which can be written as a list of comma-separated values (items) between square brackets.
Lists might contain items of different types, but usually the items all have the same type
"""

squares = [1, 4, 9, 16, 25]
print("squares:", squares)

# like strings (and all other built-in sequence types), lists can be indexed and sliced:
print(squares[0])

print(squares[-1])

print(squares[-3:])

# Lists also support operations like concatenation
squaresTmp = squares + [36, 49, 64, 81, 100]
print("squares:", squaresTmp)

# unlike strings, which are immutable, lists are a mutable types, i.e. it is possible to change their content
cubes = [1, 8, 27, 65, 125]
print("4 ** 3:", 4 ** 3)
cubes[3] = 64
print("cubes:", cubes)

# You can also add new items at the end of the list, by using the append() method (we will see more about methods later)
cubes.append(216)
cubes.append(7 ** 3)
print("cubes:", cubes)

# Assignment to slice is also possible, and this can even change the size of the list or clear it entirely
letters = ['a', 'b', 'c', 'd', 'f', 'g']
print("letters:", letters)
letters[2:5] = ['C', 'D', 'E']          # replace some value
print("letters:", letters)
letters[2:5] = []                       # now remove then
print("letters:", letters)
letters[:] = []                       # now remove all data
print("letters:", letters)

# The built-in function len() also applies to lists
letters = ['a', 'b', 'c', 'd', 'f', 'g']
print("The letters's length", len(letters))



