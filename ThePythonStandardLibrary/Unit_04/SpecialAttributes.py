"""
4.13. Special Attributes
The implementation adds a few special read-only attributes to several object types, where they are relevant. Some of
these are not reported by the dir() built-in function.

object.__dict__
    A dictionary or other mapping object used to store an object's (writable) attributes.

instance.__class__
    The class to which a class instance belongs.

class.__bases__
    The tuple of base classes of a class object.

definition.__name__
    The name of the class, function, method, descriptor, or generator instance.

    class A(object):
        pass

    a = A()
    print(A.__name__)               # A

definition.__qualname__
    The qualified name of the class, function, method, descriptor, or generator instance.

definition.__mro__
    This attribute is a tuple of classes that are considered when looking for base classes during method resolution.

class.mro()
    This method can be overridden by a metaclass to customize the method resolution order for its instances. It is called
     at class instantiation, and its result is stored in __mro__

class.__subclasses__()
    Each class keeps a list of week references to its immediate subclasses. This method returns a list of all those
    reference still alive. Example:
"""