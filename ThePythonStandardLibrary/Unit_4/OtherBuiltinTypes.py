"""
The interpreter supports several other kinds of objects. Most of these support only one or two operations.

4.12.1. Modules
The only special operation on a module is attribute access: m.name, where m is a module and name accesses a name defined
in m's symbol table. Module attributes can be assigned to. (Note that the import statement is not, strictly speaking, an
operation on a module object; import foo does not require a module object named foo to exist, rather it requireds an (
external) definition for a module named foo somewhere.)

4.12.2. Classes and class Instances
See Objects, values and types and Class definitions for these.

4.12.3 Functions
Function objects are created by function definitions. The only operation on a function object is to call it: func(
argument-list).

There are really two flavors of function objects: built-in functions and user-defined functions. Both support the same
operation (to call the function), but the implementation is different, hence the different object types.

see Function definitions for more information.

4.12.4. Methods
Methods are functions that re called using the attribute notation. There are two flavors: built-in methods (such as
append() on lists) and class instance methods. Built-in methods are described with the types that support them.

If you access a method (a funtcion defined in a class namespace) through an instance, you get a special object: a bound
method (also called instance method) object. When called, it will add the self argument to the argument list. Bound
methods have two special read-only attributes: m.__self__ is the object on which the method operators, and m.__func__ is
the function implementing the method. Calling m(arg-1, arg-2, ..., arg-n) is completely equivalent to calling m.__func__
(m.__self__, arg-1, arg-2, ..., arg-n).

Like function objects, bound method objects support getting arbitrary attributes. However, since method attributes are
actually stored on the underlying function object (meth.__func__), setting method attributes on bound methods is
disallowed. Attempting to set an attribute on a method results in an AttributeError being raised. In order to set a
method attribute, you need to explicitle set it on the underlying unction object:

"""