"""
9. Classes
    9.1 A Word About Names and Objects
    9.2 Python Scopes and Namespaces
        9.2.1 Scopes and Namespaces Example
    9.3 A First Look at Classes
        9.3.1 Class Definition Syntax
        9.3.2 Class Objects
        9.3.3 Instance Objects
        9.3.4 Method Objects
        9.3.5 Class and Instance Variables
    9.4 Random Remarks
    9.5 Inheritance
        9.5.1 Multiple Inheritance
    9.6 Private Variables
    9.7 Odds and Ends
    9.8 Iterators
    9.9 Generators
    9.10 Generator Expressions

9. Classes
Compared with other programming languages, Python's class mechanism adds classes with a minimum of new syntax and
semantics. It is a mixture of the class mechanisms found in C++ and Modula-3. Python classes provide all the
standard features of Object Oriented Programming: the class inheritance mechanism allows multiple base classes, a
derived class can override any methods of its base class or classes, and a method can call the method of a base class
with the same name. Object can contain arbitrary amounts and kinds of data. As is true for modules, classes partake of
the dynamic nature of Python: They are created at runtime, and can be modified further after creation.

In C++ terminology, normally class members (including the data members) are public ( except see below Private Variables)
, and all member function are virtual. As in Modula-3, there are no shorthands for referencing the objects's members
implicitly by the call. As in Smalltalk, classes themselves are objects. This provides semantic for importing and
renaming. Unlike C++ and Modula-3, built-in types can be used as base classes for extension by the user. Also, like in
C++, most built-in operators with special syntax (arithmetic operators, subscripting etc.) can be redefined for class
instance.

(Lacking universally accepted terminology to talk about classes, I will make occasional use of Smalltalk and C++ terms.
I would use Modula-3 terms, since its object-oriented semantics are closer to those of Python than C++, but i exception
that few readers have heard of it.)

9.1 A Word About Names and Objects
Objects have individuality, adn multiple names (in multiple) can be bound to the same object. This is known as aliasing
in other languages. This is usually not appreciated on a first glance at Python, and can be safely ignored when dealing
with immutable basic types (Numbers, Strings, Tuples). However, aliasing has a possible surprising effect on the
semantics of python code involving mutable objects such as lists, dictionaries, and most other types. This is usually
used to the benefit of the program, since aliases behave like pointers in some respects. For example, passing an object
is cheap since only a pointer is passed by the implementation; and if a function modifies an object passed as an argument,
the caller will see the change - this eliminates the need for two different argument passing mechanisms as in Pascal.

9.2 Python Scope and Namespaces
Before introducing classes, I first have to tell you something about Python's scope rules. Class definitions play some
neat tricks with namespaces, and you need to known how scope and namespaces work to fully understand what's going on.
Incidentally, knowledge about this subject is useful for any advanced Python programmer.

Let's begin with some definitions.

A namespace is a mapping from names to objects. Most namespace are currently implemented as currently implemented as
Python dictionaries, but that's normally not noticeable in any way (except for performance), and it may change in the
future. Examples of namespaces are: the set of built-in names in a function invocation. In a sense the set of attributes
of an object also from a namespace. The important thing to known about namespaces is that there is absolutely no relation
between names in different namespaces; for instance, two different modules may both difine a function maxmize without
confusion -- users of the modules must prefix must prefix it with the module name.

By the way, I use the word attribute for any name following a dot -- for example, in the expression z.real, real is an
attribute of the object z. Strictly speaking, references to names in modules are attribute references: in the expression
modname.funcname, nodname is module object and funcname is an attribute of it. in this case there happens to be a
straightforward mapping between the modules's attributes and the global names defined in the module: they share the same
namespace

Attributes may be read-only or writable. In the latter case, assignment to attributes is possible. Module attributes are
writable: you can write modname.the_answer = 42. Writable attributes may also be deleted with the del statement. For
example, del modname.the_answer will remove the attribute the answer from the object named by modname.

Namespace are created at different moments and have different lifetimes. The namespace containing the built-in names is
created when the Python interpreter starts up, and is never deleted. The global namespace for a module is created when
the module definition is read in; normally, module namespaces also last until the interpreter quits. The statements
executed by the top-level invocation of the interpreter, either read from a script file or interactively, are considered
part of a module called __main__, so they have their own global namespace. (The built-in names actually also live in a
module; this is called builtins)

The local namespace for a function is created when function is called, and deleted when function returns or raises an
exception that is not handled within the function. (Actually, forgetting would be a better way to describe what actually
happens.) Of course, recursive invocations each have their own local namespace.

A scope is a textual region of a Python program where a namespace is directly accessible. "Directly accessible" here
means that an unqualified reference to a name attempts to find the name in the namespace.

Although scope are determined statically, they are dynamically. At any time during execution, there are at least there
nested scopes whose namespaces are directly accessible:
    - the innermost scope, which is searched first, contains the local names
    - the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains
        non-local, but also non-global names
    - the next-to-last scope contains the current module's global names
    - the outermost scope (searched last) is the namespace containing built-in names

9.2.1 Scopes and Namespaces Example
"""


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After nonlocal assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, ':', x.i)
print("The real part is {0}, the image part is {1}".format(x.r, x.i))
