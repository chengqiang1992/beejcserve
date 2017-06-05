"""
3.1.2 Strings
Besides numbers, Python can also manipulate strings, which can be expressed in several ways . they
can be enclosed in single quotes('...') or double quotes("...") with the same result. \ can be used
to escape quotes
"""
print('spam eggs')
print('doesn\'t')       # use \' escape the single quote...
print("doesn't")        # ... or use double quotes instead
print("")

"""
In the interactive interpreter, the output string string is enclosed in quotes and special characters are backslashes. 
While this might sometimes look different from the input  (the enclosing quotes could change),the two string are 
equivalent. The string is enclosed in double quotes if the string contains a single quote and no double quotes, otherwise
it is enclosed in single quotes. The print() function produces a more readable output, by omitting the enclosing quotes 
and by printing escaped and special characters: 
"""

"""
String literals can span multiple lines. One way is using triple-quotes: """ """ or '''...'''. End of
lines are automatically included in the string, but it's possible to prevent this by adding a \ at the
end of the line. the following example:
备注：原来加了 \ 可以把换行取消
"""
print("""\
Usage: thingy [OPTIONS]
    -h                      Display this usage message
    -H hostname             Hostname to connect to
""")

# Strings can be concatenated (glued together) with the + operator, and repeated with *
print(3 * 'un' + 'ium')             # 3 times 'un', followed by 'ium'

"""
Two or more string literals (i.e. the ones enclosed between quotes) next to each other are
automatically concatenated
"""
print('Py' 'thon')

# This feature is particularly useful when you want to break long string:
text = ('Put several string within parentheses'
        'to have them joined together')
print(text)

# String can be indexed (subscripted), with this first character having index 0.
word = 'Python'
print(word[0])          # character in position 0
print(word[5])          # character in position 5
print(word[-1])         # last character
print(word[-2])         # second-last character
print(word[0:2])        # characters from position 0 (include) to 2 (excluded)
print(word[2:5])        # characters from position 2 (include) to 5 (excluded)
print(word[:2])         # characters from the beginning to position 2 (excluded)
print(word[4:])         # characters from the 4 (include) to the end

# print(word[42])       # the word only has 6 characters
print(word[4:42])

"""
Python string cannot be changed- they are immutable. teherefore , assigning to an indexed position
in the string result in an error
"""

# word[0] = 'J'
# print(word)
