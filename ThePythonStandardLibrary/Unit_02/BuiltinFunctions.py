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

class bytearray([Source[, encoding[, errors]]])
    Return a new array of bytes. The bytearray class is a mutable sequence of integers in the rang 0 <= x < 256. It has
    most of the usual methods of mutable sequences, described in Mutable Sequence Types, as well as most methods that
    the bytes type has, see Bytes and Bytearray Operations.

    使用场景：
        首先，bytearray 是个类，不是个函数。
        一个 int8 数组。当你对下位机交互、写网络交互底层代码、修改二进制文件时有不少的用途。
        与str(python2)、bytes(python2/3) 最大的不同在于， bytearray 是个变长的玩意，当你用 append 之类改变他的内容时
        不会像bytes那种不可变对象那样新建一个实例，而更类似于list这种可变对象，对外引用不变，然而又不同于list，
        bytearray 限制了元素的类型必须为单个字节。

    The optional source parameter can be used to initialize the array in a few different ways:
        - if it is a string, you must also give the encoding (and optionally, errors) parameters; bytearray() then
            converts the string to butes using str.encode()
        - if it is an integer, the array will have that size and will be initialized with null bytes.
        - if it is an object conforming to the buffer interface, a read-only buffer of the object will be used to
            initialize the bytes array.
        - if it is an iterable, it must be an iterable of integers in the range 0 <= x < 256, which are used as the
            initial contents of the array.
    Without an argument, an array of size 0 is created.
    see also Binary Sequence Types - bytes, bytearray, memoryview and Bytearray Object.

        a = bytearray(3)
        print(a)
        print(a[0])
        print(a[1])
        print(a[2])

        b = bytearray("abc")
        print(b)
        print(b[0])
        print(b[1])
        print(b[2])

        c = bytearray([1, 2, 3])
        print(c)
        print(c[0])
        print(c[1])
        print(c[2])

class bytes([source[, encoding[, errors]]])
    Return a new "bytes" object, which is an immutable sequence of integers in the range 0 <= x < 256. bytes is an
    immutable version of bytearray - it has the same non-mutating methods and the same indexing and slicing behavior.

    Accordingly, constructor arguments are interpreted as for bytearray().

    Bytes objects can also be created with literals, see Sting and Bytes literals.

    See also Binary Sequence Types - bytes, bytearray, memoryview, Bytes, and Bytes and Bytearray Operations.

callable(object)
    Return True if the object argument appears, False if not. if this return true, it is still possible that a call
    fails, but if it is false, calling object will never succeed. Note that classes are callable (calling a class
    returns a new instance); instance are callable if their class has a __call__() method.

    New in version 3.2: This function was first removed in Python 3.0 and then brought back in Python 3.2.

chr(i)
    Return the string representing a character whose Unicode code point is the integer i. For example, cha(97) return
    the string 'a', while chr(8364) returns the string ''. this is the inverse of ord().

        print(chr(97))      # 'a'
        print(ord('a'))     # 97

classmethod(function)
    Return a class method for function
    类方法
    普通方法  类方法  静态方法

compile(source, filename, mode, flags = 0, dont_inherit=False, optimize=-1)
    Compile the source into a code or AST object. Code objects can be executed by exec() or eval().


delattr(object, name)
    This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of the
    object's attributes. The function deletes the named attribute, provided the object allows it. For example,

    delattr(x, 'foobar') is equivalent to del x.foovar

class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
    Create a new dictionary. The dict object is the dictionary class. See dict and Mapping Types - dict for
    documentation about this class.

    For other containers see the built-in list, set and tuple classes, as well as the collections module.

    ----------------------------------------------NOTICE----------------------------------------------------------------
    class dict(**kwarg)
    class dict(mapping, **kwarg)
    class dict(iterable, **kwarg)
        Return a new dictionary initialized from an optional positional argument and a possibly empty set of keyword
        arguments.

        If no positional argument is given, an empty dictionary is created. If a positional argument is given and it is
        a mapping object, a dictionary is created with the same key-value pairs as the mapping object. Otherwise, the
        positional argument must be an iterable object. Each item in the iterable must iterable with exactly two objects
        The first object of each item becomes a key in the new dictionary, and the second object the corresponding value.
        If a key occurs more than once, the last value for that key become the corresponding value in the new dictionary.

        If keyword arguments are given, the keyword arguments and their values are added to the dictionary created form
        the positional argument. If a key being added is already present, the value from the keyword arguments replaces
        the value from the positional argument.

        To illustrate, the following examples all return a dictionary equal to {"one": 1, "two": 2, "three": 3}

            a = dict(one=1, two=2, three=3)
            b = {'one': 1, 'two': 2, 'three': 3}
            c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
            d = dict([('two', 2), ('one', 1), ('three', 3)])
            e = dict({'three': 3, 'two': 2, 'one': 1})

            print(a)        # {'one': 1, 'two': 2, 'three': 3}
            print(b)        # {'one': 1, 'two': 2, 'three': 3}
            print(c)        # {'one': 1, 'two': 2, 'three': 3}
            print(d)        # {'two': 2, 'one': 1, 'three': 3}
            print(e)        # {'three': 3, 'two': 2, 'one': 1}
            print(a == b == c == e)     # True

dir([object])
    Without arguments, return the list of names in the current local scope. With an arugument, attempt to return a list
    of valid attributes for that object.

    If the object has a method named __dir__(), this method will be called and must return the list of attributes. This
    allows objects that implement a custom __getattr()__ or __getattribute__() function to customize the way dir()
    reports their attributes.

    If the object does not provide __dir__(), the function tries its best to gather information from the object's
    __dict__ attribute, if defined, and from its type object. The resulting list is not necessarily complete, and may be
    inaccurate when the object has a custom __getattr__().

divmod(a, b)
    Take two (non complex) numbers as arguments and return  a pair of numbers consisting of their quotient and remainder
    when using integer division.  With mixed operand types, the rules for binary arithmetic operators apply. For
    integers, the result is the same as (a//b, a % b). For floating poing numbers the result is (q, a % b), where q is
    usually math.floor(a / b) but may be 1 less than that. In any case q＊ｂ＋a%b is bery close to a, if a%b is non-zero
    it has the same sign as b, and 0 <= abs(a%b) < abs(b).
    本函数是实现a除以b，然后返回商与余数的元祖。如果两个参数a，b都是整数，那么会采用整数除法，结果相当与 ( a//b, a%b).
    如果a或b是浮点数，相当于(math.floor(a/b), a%b)

enumerate(iterable, start=0)
    Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.
    The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which
    defaults to 0) and the values obtained from iterating over iterable.

    今天发现一个新函数 enumerate。一般情况下对一个列表或数组既要遍历索引又要遍历元素时，会这样写：

eval(expression, global=None, local=None)
    The arguments are a string and optional global and locals. If provided, globals must be a dictionary. If provided,
    locals can be any mapping object.

    The expression arguments is parsed and evaluated as a Python expression (technically speaking, a condition list)
    using the globals and locals dictionaries as global and local namespace. if the globals dictionary is present and
    lacks '__

exex(object[, global[, locals]])
    This function supports dynamic of Python code. Object must be either a string or a code object. If it is a string,
    the string is parsed as a suit of Python statements which is then executed  (unliess a syntax error occurs). If it
    is a code object, it is simply executed. In all cases, the code that's executed is expected to be valid as file
    input (see the section "File input") in the Reference Manual). Be aware that the return and yield statements may not
    be used outside

filter(function, iterable)
    Construct an iterable from those elements of iterable for which function returns true. iterable may be either a
    sequence, a container which supports iteration, or an iterator. If functions is None, the identify function is
    assumed, that is, all elements of iterable that are false are removed.

    Note that filter (function, iterable) is equivalent to the generator expression (item for item in iterable if
    function(item)) if function is not None and (item for item in iterable if item) if function is None.

"""






















