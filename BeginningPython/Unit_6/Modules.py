"""
6. Modules
if you quit from the Python interpreter and enter it again. the definitions you have made (functions and
variables) are lost. Therefore, if you want to write a somewhat longer program, you are better
off using a text editor to prepare the input for the interpreter and running it with that file as input instead.
this is known as creating a script. As your program gets longer, you may want to split it into several
files for easier maintenance. You many also want to use a handy function that you;ve written in several programs
without coping its definition into each program

To support this, Python has a way to put definitions in a file and use them in a script or in an
interactive instance of the interpreter. Such a file is called a module; definitions from a module
can be imported into other modules or into the main modules (the collection of variables that you have
access to in a script executed at the top level and in calculator mode)

A modules is file containing Python definitions and statements. The file name is the module name with
the suffix .py appended. Within a module, the modules's name (as s string) is available as the
value of the global variable __name__. For instance, use your favorite text editor to create
a file called fibo.py in the current directory with the following contents:
"""

"""
6.1 More on Modules
A module cna contain executable statements as well as function definitions. These statements
are intended to initialize the module. They are executed only the first time the module name
is encountered in an import statement. (They are also run if the file is executed as a script)

Each module has its own private symbol table, which is used as the global symbol table by all
functions defined in the module. thus the author of a module can use global variables in the module
without worrying about accidental clashes with a user's global variables. on the other hand,
if you know what you are doing you can touch a module's global variables with the same notation used
to refer to its functions, modname.itemname.

modules can import other modules. It is customary but not required to place all import statement at
the beginning of a module (or script, for that matter). the imported module names are placed in
the importing modules's global symbol table.
"""

from .fibo import *
fib(200)