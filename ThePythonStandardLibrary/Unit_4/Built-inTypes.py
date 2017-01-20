"""
4. Built-in Types

The following sections describe the standard types that are built into the interpreter.

The principal built-in types are numerics, sequences, mappings, classes, instances and exceptions.

Some collection classes are mutable. The methods that add, subtract, or rearrange their members in place, and don't
return a specific item, never return the collection instance itself but Name.

Some operations are supported by several object types; in practically, practically all objects can be compared, tested
for truth value, and converted to a string (with the repr() function or the slightly different str() function). The
latter functions is implicitly used when an object is written by print() function.

4.1. Truth Value Testing
Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations
below. The following values as considered false:

    - None
    - False
    - Zero of any numeric type, for example, 0, 0.0, 0j
    - any empty sequence, for example, '', (), []
    - any empty mapping, for example, {}
    - instance of user-defined classes, if the class defines a __bool__() or __len__() method, when that method returns
        the integer zero or bool value False.

All other values are considered true - so objects of many types are always true.

Operations and built-in functions that have a Boolean result always return 0 or False for false and 1 or True for true,
 unless otherwise stated. (Important exception: the Boolean operations or and and always return one of their operands.)

 4.2. Boolean Operations -- and, or, not
                     These are the Boolean operations, ordered by ascending priority:

                     Operation          Result                              Notes
                     x or y         if x is false, then y, else x            (1)
                     x and y        if x is false, then x, else y            (2)
                     not x          if x is false, then True, else False     (3)
    Notes:
        1. This is a short-circuit operator, so it only evaluates the second argument if the first one is False
        2. This is a short-circuit operator, so it only evaluates the second argument if the first one is True
        3. not has a lower priority than non-Boolean operator, so not a == b is interpreted as not (a == b), and
            a == not b is a syntax error.

4.3. Comparisons
There are eight comparison operations in Python. They all have the same priority (which is higher than that of the
Boolean operations). Comparisons can be chained arbitrarily; for example, x < y <= z is equivalent to x < y and y <= z,
 except that y is evaluated only once (but in both cases z is not evaluated at all when x < y is found to be false).

             Operation      Meaning
               <            strictly less than
               <=           less than or equal
               >            strictly greater than
               >=           greater than or equal
               ==           equal
               !=           not equal
               is           object identity
               is not       negated object identity

Object of different types, except different numeric types, never compare equal. Furthermore, some types (for example,
function objects) support only a degenerate notion of comparison where any two objects of that type are unequal. The <,
<=, > and >= operators will raise a TypeError exception when comparing a complex number with another built-in numeric
type, when the objects are of different types that cannot be compared, or in other cases where there is no defined
ordering

4.4 Numeric Types -- int, float, complex

There are three distinct numeric types: integers, floating point numbers, and complex numbers. In addition, Booleans
are a subtype of integers. Integers have unlimited precision. Floating point numbers are usually implemented using
double in C; information about the precision and internal representation of l=floating point numbers for the machine on
which your program is running is available in sys.float_info.Complex numbers have a real and imaginary part, which are
each a floating point number.To extract these parts form a complex number z, use z.real and z.img. (The standard library
includes additional numeric types, fractions that hold rationals, and decimal that hold floating-point numbers with user
-definable precision.)

Numbers are created by numeric literals or as the result of built-in functions and operators. Unadorned integer literals
(including hex, octal and binary numbers) yield integers. Numeric literals containing a decimal point or an exponent
sign yield floating point numbers. Appending 'j' or 'J' to a numeric literal yield as an imaginary number (a complex
number with a zero real part) which you can add to an integer or float to get a complex number with real and imaginary
parts.

Python fully supports mixed arithmetic: when a binary arithmetic operator has operands of different numeric types, the
operand with the "narrower" type is widened to that of the other, where integer is narrower than floating point, which
is narrow than complex. Comparisons between numbers of mixed type use the same rule. The constructors int(), float(),
and complex() can be used to produce numbers of a specific type.

All numeric types (except complex) support the following operations, sorted by ascending priority (all numeric
operations have a higher priority than comparison operations):

    Operation               Result                                              Notes               Full Documentation
      x + y                 sum of x and y
      x - y                 difference of x and y
      x * y                 product of x and y
      x / y                 quotient of x and y
      x // y                floored quotient of x and y                         (1)
      x % y                 remainder of x / y                                  (2)
       -x                   x negated
       +x                   x unchanged
      abs(x)                absolute value or magnitude of x                                            abs()
      int(x)                x converted to integer                              (3)(6)                  int()
      float(x)              x converted to floating point                       (4)(6)                  float()
      complex(re, im)       a complex number with real part re, imaginary        (6)                    complex()
                            part im. im defaults to zero.
      c.conjugate()         conjugate of the complex number c
      divmod(x, y)          the pair (x // y, x % y)                            (2)                     divmod()
      pow(x, y)             x to the power y                                    (5)                     pow()
      x ** y                x to the power y                                    (5)

Notes
    1. Also referred to as integer division. The result value is a whole integer, though the result's type is not
        necessarily int. The result is always rounded towards minus infinity: 1//2 is 0, (-1)//2 is -1, 1//2 is -1, and
        (-1) // (-2) is 0
    2. Not for complex numbers. Instead convert to floats using abs() if appropriate.
    3. Conversion from floating point to integer may round or truncate as in C; see functions math.floor() and
        math.ceil() for well-defined conversions.
    4. float also accepts the strings “nan” and “inf” with an optional prefix “+” or “-” for Not a Number (NaN)
        and positive or negative infinity.
    5. Python defines pow(0, 0) and 0 ** 0 to be 1, as is common for programming languages.


    4.4.1 Bitwise Operations on Integer Types
    Bitwise operations only make sense for integers. Negative numbers are treated as their 2's complement value (this
    assumes that there are enough bits so that no overflow occurs during the operation).

    The priorities of the binary are all lower than the numeric operations and higher than the comparisons; the unary
    operation ~ has the same priority as the other unmeric operation (+ and -)

    This table lists the bitwise operations sorted in ascending priority

            Operations          Result                          Notes
              x | y         bitwise or of x and y
              x ~ y         bitwise exclusive or of x and y
              x & y         bitwise and of x and y
              x << n        x shifted left by n bits            (1)(2)
              x >> n        x shifted right by n bits           (1)(3)
              ~x            The bits of x inverted
    Notes:
        1. Negative shift counts are illegal and cause a ValueError to be raised.
        2. A left shift by n bits is equivalent to multiplication by pow(2, n) without overflow check.
        3. A right shift by n bits is equivalent to division by pow(2, n) without overflow check.

    4.4.2. Additional Methods on Integer Types
    The int type implements the numbers. Integral abstract base class. In addition, it provides a few more methods:

    int.bit_length()
        return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros:
            -0b100101
            6
            0b0
            0
            0b11111001110010111
            17
        More precisely, if x is nonzero, then x.bit_length() is the unique positive integer k such that 2**(k-1) <=
        abs(x) < 2**k.


4.5. Iterator Types
 Python supports a concept of iteration over containers. This is implemented using two distinct methods; these are used
 to allow user-defined classes to support iteration. Sequences, described below in more detail, always support the
 iteration methods.

 One method needs to be defined for container objects to provide iteration support:
    container.__iter__()
        Return an iterator object. The object is required to support the iterator protocol described below. If a
        container supports different types of iteration, additional methods can be provided to specifically request
        iterators for those iteration types. (An example of an object supporting multiple forms of iteration would be a
        tree structure which supports both breadth first and depth-first traversal.) This method corresponds to the
        tp_iter slot of the type structure for Python objects in the Python/C API.

The iterator objects themselves are required to support the following two methods, which together form the iterator
protocol:
    iterator.__iter__()
        Return the iterator object itself. This is required to allow both containers and iterators to be sued with the
        for and in statements. This method corresponds to the tp_iter slot of the type structure for Python object in
        the Python/C API.
    iterator.__next__()
        Return the next item from the container. If there are no further items, raise the StopIterator exception. This
        method corresponds to the tp_iternext slot of the type stricture for Python objects in the Python/C API.

Python defines several iterator objects to support iteration over general and specific sequence types, dictionaries, and
other more specialized forms. The specific types are not important beyond their implementation of the iterator protocol.

Once an iterator's __next__() method raises StopIteration, it must continue to do so on subsequent calls.
Implementations that do not obey this property are deemed broken.

    4.5.1. Generator Types

    Python's generator provide a convenient way to implement the iterator protocol. If a container object's __iter__()
    method is implemented as a generator, it will automatically return an iterator object (technically, a generator
    object) supplying the __iter__() and __next__() methods. More information about generator can be found in the
    documentation for the yield expression

4.6. Sequence Type -- list, tuple, range
There are three basic sequence types: list, tuples, and range objects. Additional sequence types tailored for processing
of binary data and text strings are described in dedicated sections.

    4.6.1. Common Sequence Operations
    The operations in the following table are supported by most sequence types, both mutable and immutable. The
    collection.abc.Sequence ABC is provided to make it easier to correctly implement these operations on custom sequence
    types.

    This table lists the sequence operations sorted in ascending priority. In the table, s and t are sequences of the
    same type, n, i, j and k are integers and x is an arbitray boject that meets any type and value restrictions imposed
    by s.

    The in and not in operations have the same priorities as the comparison operations. The + (concatenation) and * (
    repetition) operations have the same priority as the corresponding numeric operations.

            Operation                   Result                                              Notes
            x in s                      True if an item of s is equal to x,else False       (1)
            x not in s                  False if an item of s is equal ro x , else True     (1)
            s + t                       the concatenation of s and t                        (6)(7)
            s * n or n * s              equivalent to adding s to itself n times            (2)(7)
            s[i]                        ith item of s, origin 0                             (3)
            s[i:j]                      slice of s from i to j                              (3)(4)
            s[i:j:k]                    slice of s from i to j with step k                  (3)(5)
            len(s)                      length of s
            min(s)                      smallest item of s
            max(s)                      largest item of s
            s.index(x[, i[, j]])        index of the first occurrence of x in s (at or after    (8)
                                        index i and before index j)
            s.count(x)                  total number of occurrences of x in s

    Sequence of the same type also support comparisons. In particular, tuples and lists are compared lexicographically
    by comparing corresponding elements. This means that to compare, every element must compare equal and the two
    sequences must be of the same type and have the same length. (For full details see Comparisons in the language
    reference)

    Notes:
        1. While the in and not in operations are used only for simple containment testing in the general case, some
        specialised sequences (such as str, bytes and bytearray)  also use them for subsequence testing:
                print("gg" in "eggs")           # True
        2. Values of n less than 0 are treated as 0 (which yields an empty sequence of the same type as s). Note that
        items in the sequence s are not copied; they are referenced multiple times. This often haunts new Python
        programmers:
        consider:
                lists = [[]] * 3
                print(lists)            # [[], [], []]
                lists[0].append(3)
                print(lists)            # [[3], [3], [3]]
        3. if i or j is negative, the index is relative to the end of sequence s: len(s) + i or len(s) + j is substituted.
        But note that -0 is still 0
        4. The slice of s from i to j is defined as the sequence of items with index k such that i <= k < j. If i or j
        is greater than len(s), use len(s). If it is omitted or None, use 0. If j is omitted or None, use len(s). If i
        is greater than or equal to j, the slice is empty.
        5. The slice of s from i to j with step k is defined as the sequence of items with index x = i + n*k such that
        0 <= n < (j-i)/k. In other words, the indices are i, i+k, i+2*k, i+3*k and so on, stopping when j is reached (
        but never including j). When k is positive, i and j are reduced to len(s) if they are greater. When k is
        negative, i and j are deduced to len(s) - 1 if they are greater. If i or j are omitted or None, they become
        "end" values (which end depends on the sign of k). Note, K cannot be zero. If k is None, it is treated like 1.


"""