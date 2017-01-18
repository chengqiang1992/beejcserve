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
"""