"""
3. Built-in Constants

A small number or constants live in the built-in namespace. They are:

False
    The false value of the bool type. Assignments to False are illegal and raise a SyntaxError

True
    The true value of the bool type. Assignments to True are illegal and raise a SyntaxError

None
    The sole value of the type NoneType. None is frequently used to represent the absence of a value, as when default
    arguments are not passed to a function. Assignments to None are illegal and raise a SyntaxError

NotImplemented
    Special value which should be returned by the binary special methods (e.g. __eq_(), __lt__(), __add__(), __rsub__(),
    etc) to indicate that the operation is not implemented with respect to the other type; may be returned by the
    in-place binary special methods (e.g. __imul__(), __iand__(), tec.)for the same purpose. Its truth value is true.

    Note: NotImplementedError and NotImplemented are not interchangeable, even though they have similar names and
    purposes. See NotImplementedError for details on when to use it.

    NOTE: NotImplementedError and NotImplemented 区别
    NotImplemented 是一个非异常对象，NotImplementedError 是一个异常对象。
        print(NotImplemented)               # NotImplemented
        print(NotImplementedError)          # <class 'NotImplementedError'>
        print(type(NotImplemented))         # <class 'NotImplementedType'>
        print(type(NotImplementedError))    # <class 'type'>

    如果抛出 NotImplemented 会得到 TypeError, 因为它不会一个异常。而抛出 NotImplementedError 会正常补货该异常

    为什么要存在一个 NotImplemented 和一个 NotImplementedError 呢？
        在 Python 中对列表进行排序时，会经常间接使用像 __It__() 这类比较运算的方法。
        有时 Python 的内部算法会选择别的方法来确定比较结果，或者直接选择一个默认的结果。如果抛出一个异常，则会打破排序
        运算，因此如果使用 NotImplemented 则不会抛出异常，这样 Python 可以尝试别的方法。

        NotImplemented 对象向运行时环境发出一个信号，告诉运行环境如果当前操作失败，他应该再检查一下其他可行方法。例如在
        a == b 表达式， 如果 a._eq_(b) 返回 NotImplemented， 那么 Python 会尝试 b._eq_(a). 如果调用b的 _eq_() 方法可以
        返回 True 或者 False， 那么该表达式就成功了。如果b._eq_(a) 也不能的出结果， 那么 Python 会继续尝试其他方法，例如
        使用 ！= 来比较。

Ellipsis
    The same as ... Special value used mostly in conjunction with extended slicing syntax for user-defined container
    data types.

__debug__
    This constant is true if Python was not started with an -o option, See also the assert statement.

3.1. Constants added by the site module
    The site module (which is imported automatically startup, except if the -S command-line option is given) adds
    several constants to the built-in namespace. They are useful for the interactive interpreter shell and should not be
    used in programs.

    quit(code=None)
    exit(code=None)
    copyright
    license
    credits
"""
