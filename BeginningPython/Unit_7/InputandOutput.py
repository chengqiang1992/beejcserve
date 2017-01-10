"""
7. Input and Output
There are several ways to present the output of a program; data can be printed in a human-readable form, or written to
a file for future use. This chapter will discuss some of the possibilities.

7.1 Fancier Output Formatting
So far we've encountered two ways of writing values: expression statements and the print() function. (
A third way is using the waite() method of file object: the standard output file can be referenced as
sys.stdout. See the Library Reference for more information on this.)

Often you'll want more control over the formatting of your output than simply printing space-separated
values. There are two ways to format your output; the first way is to do all the string handling yourself;
using string slicing and concatenation operations you can create any layout you can imagine. The string
type has some methods that perform useful operations for padding string to a given column width; these will
be discussed shortly. The second way is to use formatted string literals, or the str.format() method.

The string module contains a Template class which offers yet another way to substitute values strings.

One question remains, of course: how do you convert values to strings? Luckily, Python has ways to convert
 any value to a string: pass it to the repr() pr str() functions.

 The str() functions is meant to return representations of values which are fairly human-readable, while
 repr() is meant to generate representations which can be read by the interpreter (or will force a SyntaxError
 if there is no equivalent syntax). For objects which don't have a particular representations for human
 consumption, str() will return the same value as repr(). Many values, such as numbers or structures like lists
 and dictionaries, have the same representation using either function. Strings, in particular, have two distinct
 representations

 some examples:
"""

import math

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print(' {0:5d} {1:5d} {2:10d}'.format(x, x*x, x*x*x))

"""
(Note that in the first example, one space between each column was added by the way print() works: it always adds
spaces between its arguments.)

This example demonstrates the str.rjust() method of string objects,which right-justifies a string in a field of a
given width by padding ot with spaces on the left. There are similar methods str.ljust() and str.center(). These
methods do not write anything, they just return a new string. If the input string is to long, they don'y truncate it,
"""

# There is another method, str.zfill(), which pads a numeric string on the left with zeros. it understands about plus
# and minus signs:
print('12'.zfill(5))
print('-3.13'.zfill(7))
print('3.14159265359'.zfill(5))

# Basic usage of the str.format() method looks like this:
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

"""
The brackets and characters within them (called format fields) are replaced with the objects passed into the str.formate()
method. A number in the brackets can be used to refer to the positions of the object passed into the str.formate() method()
"""

print('{0} and {1}'.format('spam', 'egg'))      # 位置方法
print('{1} and {0}'.format('spam', 'egg'))

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

# '!a' (apply ascii())  '!s'(apply str) and '!r'(apply repr()) can be used to convert the value before it is formatted


# Old string formatting

print('The value of PI is approximately %5.3f.' % math.pi)

