"""
8. Errors and Exceptions
Util now error messages  haven't been more mentioned, but if you have tried out the examples you have
 probably seen some. There are (at least) two distinguishable kinds of error: syntax and exceptions

8.1 Syntax Errors
Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while
you are still learning Python:

while True print('Hello world')

The parser repeats the offending line and displays a little 'arrow' pointing at the earliest point in
the line where the error was detected. the error is caused by (or at least detected at) the token preceding
the arrow: in the example, the error is detected at the function print(), since a colon (':') is missing
before it. File name and line number are printed so you know where to look in case the input came from a script

8.2 Exceptions
Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to
execute it. Errors detected during execution are called exceptions and are not unconditionally fatal: you will
soon learn how to handle them in Python programs. Most exceptions are not handled by programs, however, and result
in error messages as known here

The last line of the error message indicates what happened. Exceptions come in different types, adn the type is
printed as part of the message: the types in the example are ZeroDivisionError, NameError and TypeError. The string
printed as the exception type is the name of the built-in exception that occurred. This is true for all built-in
exceptions, but need not be true for user-defined exceptions (although it is a useful convention). Standard exception
names are built-in identifiers (not reserved keywords).

The rest of the line provides detail based on the type of exception and what caused it.

The preceding part of the error message shows the context where the exception happened, in the form of a stack traceback
In general it contains a stack traceback listing source lines; however, it will not display lines read from standard input.


8.3 Handling Exceptions
It is possible to write programs that handle selected exceptions. Look at the following example, which ask the user for input
until a valid integer has been entered, but allows the user to interrupt the program. note that a user-generated
interruption is signalled by raising the KeyBoardInterrupt exception
"""

import sys


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")

"""
The try statement works as follows.
    1: First, the try clause (the statement(s) between the try and except keywords) is executed.
    2: if no exceptions occurs, the except clause is skipped and execution of the try statement is finished
    3: if an exception occurs during exception of the try clause, the rest of the clause is skipped. Then if its
    type matches the exception named after the except keyword, the except clause is executed, and then execution
    continues after the try statement.
    4: if an exception occurs which does not match the exception named in the except clause, it is passed on to outer
    try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown
        above

A try statement may have more than one except clause, to specify handlers for different exceptions. At most one handler
will be executed. Handlers only handle exceptions that occur in the corresponding try clause, Not in other handlers of
the same try statement. An except clause may name multiple exceptions as a parenthesized tuple, for example

 :except(RuntimeError, TypeError, NameError):
    pass

A class in an except clause is compatible with an exception if it is the same class or a base class thereof (but not the
the other way around - an except clause listing a derived class is not compatible with a base class). For example, the
following code will print B, C, D in that order:
"""


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

"""
The last except clause may omit the exception name(s), to serve as a wildcard. Use this with extreme caution, since it
is easy mask a real programming error in this way! It can also be used to print an error message and then re-raise the
exception (allowing a caller to handle the exception as well)
"""


try:
    f = open("myfile.txt", 'r')
    print(f)
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print(("OS error: {0}".format(err)))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

""""
The try...except statement has an optional else clause, which, when present, must follow all except clause. It is useful
for code that must be excepted if the try clause does not raise an exception.
"""
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readline(), 'lines'))
        f.close()

"""
The use of the else clause is better than adding additional code to the try clause because of avoids accidentally
catching an exception that wasn't raised by the code being protected by rhe try...catch statement

when an exception occurs, it may have an associated value, also known as the exception's argument. the presence and type
of the argument depend on the exception type.
"""

"""
8.4 Raising Exceptions
The raise statement allows the programmer to force a specified exception to occur. For example.

raise NameError('HiThere')

The sole argument to raise indicates the exception to gbe raised. This must be either an exception instance or an
exception class (a class that derives from Exception). If an exception class is passed, It will be implicitly by calling
its constructor with no argument:

try:
    raise NameError('HiThere')
exception NameError:
    print('An exception flew by!')
    raise
"""

""""
8.5 User-defined Exceptions
Programs may name their own exceptions by creating a new exception class (see Classes for more about Python classes).
Exceptions should typically be derived from the Exception class, either directly or indirectly.

Exception classes can be defined which do anything any other class can do, but are usually kept simple, often only
offering a number of attributes that allow information about the error to be extracted bu handlers for the exception.
when creating a module that can raise several distinct errors, a common practice is to crate a bse class for
exceptions defined by that module, and subclass that to create specific exception class for different error conditions:
"""


class Error(Exception):
    """Base class for exception in this module"""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occured
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message =  message

class TransitionError(Error):
    """
    Raised when an operation attempts a state transition that' not allowed
    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of thwy the specific transition is not allowed
    """
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

