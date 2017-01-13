"""
11. Brief Tour of the standard Library - Part II
This second tour covers more advanced modules that support professional needs. These modules rarely occur in small
scripts.
"""

import reprlib
import pprint
import textwrap
import locale
from string import Template

"""
11.1 Output Formatting
The reprlib module provides a version of repr() customized for abbreviated displays of large or deeply nested containers
"""

print(reprlib.repr(set('supercalifragilisticexpialidocious')))


# class MyList(list):
#     @recursive_repr()
#     def __repr__(self):
#         return '<' + "|".join(map(repr, self)) + '>'
#
# m = MyList('abc')
# m.append(m)
# m.append('x')
# print(m)

"""
The pprint module offers more sophisticated control over printing both built-in and user defined objects in a way that
is readable by the interpreter. When the result is longer than one line, the "pretty printer" adds line breaks and
indentation to more clearly reveal data structure:
"""
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=30)

# The textwrap module formats paragraphs of text to fit a given screen width
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))

"""
The local module accesses a database of culture specific data formats. The grouping attribute of locale's format
function provides a direct way of formatting numbers with group separators:
"""
locale.setlocale(locale.LC_ALL, 'English_united States.1252')
print(locale.setlocale(locale.LC_ALL, 'English_united States.1252'))
conv = locale.localeconv()
x = 1234567.8
locale.format('%d', x, grouping=True)
print(locale.format('%d', x, grouping=True))
locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True)
print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))

"""
11.2 Templating
The string module includes a versatile Template class with a simplified syntax for editing by end-users. This allows
users to customize their applications without having to alter the application

The format uses placeholder names formed by $ with valid Python Identifiers (alphanumeric characters and underscores).
Surrounding the placeholder with braces allows it to be followed by more alphanumeric letters with no intervening spaces.
Writing $$ creates a single escaped $:
"""

t = Template('${village} folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')
print(t.substitute(village='Nottingham', cause='the ditch fund'))

