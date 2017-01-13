"""
10. Brief Tour of the Standard Library
10.1 Operating System Interface
The os module provides dozens of functions for interacting with the operating system:
"""
import os
import glob

print(os.getcwd())
os.chdir('D:\BackEnd\LearnPython\GoodCode')
print(os.getcwd())
os.system('mkdir today')
"""
Be sure to use the import os style instead of from os import *. This will keep os.open() from shadowing the
built-in open() function which operates much differently

The built-in dir() and help() functions are useful as interactive aids for working with large modules like os
"""
# print(dir(os))
# print(help(os))

# For daily file and directory management tasks, the shutil module provides a height llevel interface that is easier to
# use

# 10.2 File Wildcards
# The global module provides a function for making file lists from directory wildcards searches:
os.chdir('D:\BackEnd\LearnPython\BeginningPython')
print(os.getcwd())
# print(glob("*/*.py"))

"""
10.3 Command Line Arguments
Common utility scripts often need to process command line arguments. These arguments are stored in the sys module's argv
attributes as a list. For instance the following output results from running python demo.py on two three at the command
line:
"""

"""
10.4 Error Output Redirection and Program Termination
The sys module also has attributes for stdin, stdout, and stderr. The latter is useful for emitting warning and error
messages to make them visible even when stdout has been redirected:
"""

"""
10.5 String Pattern Matching
There re module provides regular expression tools for advanced string processing. For complex matching and manipulation,
regular expressions offer succinct, optimized solutions:
"""

"""
10.6 Mathematics
The math module gives access to the underlying C library functions for floating pint math:

The random modules provides tools for making random selections:

The statistics module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data:
"""

"""
10.7 Internet Access
There are a number of modules for accessing the internet and processing internet protocols. Two of the simplest are
urllib.request for retrieving data from URLs and smtplib for sending mail:
"""

"""
10.8 Dates and Times
The datetime modules supplies classes for manipulating dates and times in both simple and complex ways. While date and
time arithmetic is supported, the focus of the implementation is on efficient member for output formatting and
manipulation. The module also supports objects that are timezone aware.
"""

"""
10.9 Date Compression
Common data archiving and compression formats are directly supported by modules including: zlib, gzip, bz22, lzma,
zipfile and watfile.
"""

"""
10.10 Performance Measurement
Some Python users develop a deep interest in knowing the relative performance of different approaches to the same
problem. Python provides a measurement tool that answers those questions immediately.

For example, it may be tempting to use the tuple packing and unpacking feature instead of the traditional approach to
swapping arguments. The timeit module quickly demonstrates a modest performance advantage:
"""

"""
10.11 Quality Control
One approach for developing high quality software is to write tests for each functions as it is developed and to run
those tests frequently during the development process.

The doctest module provides a tool for scanning a module and validating tests embedded in a program's docstrings. Test
construction is as simple as cutting-and-pasting a typical call along with its result into the docstring. This improves
the documentation by providing the user with an example and it allows the doctest module to make sure the code remains
true to the document:

The unittest module is not as effortless as the doctest module, but it allows a more comprehensive set of tests to be
maintained in a separate file
"""

"""
10.12 Batteries Included
Python has a "batteries included" philosophy. This is best seen through the sophisticated and robust capabilities of its
larger package. For example:

    The xmlrpc.client and xmlrpc.sever modules make implementing remote procedure calls into an almost trivial task.
        Despite the modules name, no direct knowledge or handling of XML is needed.
    The email package is a library for managing email messages, including MIME and other RFC 2822-bsaed message
        documents. Unlike smtplib and poplib which actually send and receive message, the email package has a complete
        toolset for building or decoding complex message structures and for implementing internet encoding and header
        protocols.
    The json package provides robust support for parsing this popular data interchange format. The CSV module supports
        direct reading and writing of files in comma-separted value format
    The sqlite3 module is a wrapper for the SQLLite datanase library.
"""


