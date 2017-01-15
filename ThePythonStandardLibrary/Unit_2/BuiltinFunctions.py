"""
2. Built-in Functions
The Python interpreter has a number of functions and typepes built into it that are always available. They are listed
here in alphabetical  order.

                        Built-in Functions

abs()           dict()          help()          min()           setattr()
all()           dir()           hex()           next()          slice()
any()           divmod()        id()            object()        sorted()
ascii()         enumerate()     input()         oct()           staticmethod()
bin()           eval()          int()           open()          str()
bool()          exec()          isinstance()    ord()           sum()
bytearray()     filter()        issubclass()    pow()           super()
bytes()         float()         iter()          print()         tuple()
callable()      format()        len()           property()      type()
chr()           frozenset()     list()          range()         vars()
classmethod()   getattr()       locals()        repr()          zip()
compile()       globals()       map()           reversed()      __import__()
complex()       hasattr()       max()           round()
delattr()       hash()          memoryview()    set()

abs(x)
    Return the absolute value of a number. The argument may be an integer or a floating point number. if the arguments is
    a complex number, its magnitude is returned

all(iterable)
    Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:
    def all(iteralbe):
    for element in iteralbe:
        if not element:
            return False
    return True

any(iterable)
    Return True if any element of the iterable is true. if the iterable is empty, return False. Equivalent to:

    def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

    +---------------------------------------------+-------------+---------------+
    |                                                   any             all     +
    +---------------------------------------------+-------------+---------------+
    |   All Truthy values                               True            True    +
    +---------------------------------------------+-------------+---------------+
    |   All Falsy values                                False           False   +
    +---------------------------------------------+-------------+---------------+
    |   One Truthy value (all others are Falsy)         True            False   +
    +---------------------------------------------+-------------+---------------+
    |   One Falsy value (all others are Truthy)         False           False    +
    +---------------------------------------------+-------------+---------------+
    |   Empty Iterable                                  False           True    +
    +---------------------------------------------+-------------+---------------+


ascii(object)
    As repr(), return a string containing a printable representation of an object, but escape the non-ASCII characters
    in the string returned by repr() using \x, \u or \U escape. This generates a string similar to that returned by
    repr() in Python 2.

    print(ascii(10))            # 10
    print(ascii('b\12'))        # 'b\n'
    print(ascii('b\13'))        # 'b\x0b'
    print(ascii('0x\1000'))     # '0x@0'

bin(x)
    Convent an integer number to a binary string. The result is a valid Python expression. If x is not a Python int
    object, it has to define an __index__() method that returns an integer.

    print(bin(10))
    print(bin(16))

class bool([x])
    Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure. if x
    is false or omitted, this returns False; otherwise it returns True. The bool class is a subclass of int (see Numeric
    Types - int, float, complex). It cannot be subclassed  further. Its only instances are False and True (see Boolean
    Values).

                        Truth Value Testing
        Any Object can be tested for truth value, for use in an if or while condition or as operand of the Boolean
        operations below. The following values are considered false:
        - None
        - False
        - zero of any numeric type, for example, 0, 0.0, 0j
        - any empty sequence, for example, '', (), []
        - any empty mapping, for example, {}
        - instance of user-defined classes, if the class defines a __bool()__ or __len()__ method, When that method
            returns the integer zero or bool value False
        All other values are considered true - so objects of many types are always true.
        Operations and built-in functions that have a Boolean result 0 or False for false and 1 or True for true,
"""



