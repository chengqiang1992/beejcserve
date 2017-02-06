"""
BaseException                                                               所有异常基类
    +- SystemExit                                                           Python 解释器请求推出
    +- KeyboardInterrupt                                                    用户中断执行（通常是输入ctrl+c）
    +- GeneratorExit                                                        生成器（generator）发生异常来通知推出
    +- Exception                                                            常规错误的基类
        +- StopIteration                                                    迭代器没有更多的值
        +- StandardError                                                    所有的内建标准异常的基类
        |   +- BufferError
        |   +- ArithmeticError                                              所有数值计算错误的基类
        |   |   +- FloatingPointError                                       浮点计算错误
        |   |   +- OverflowError                                            数值运算超出最大限制
        |   |   +- ZeroDivisionError                                        除（或取模）零（所有数据类型）
        |   +- AssertionError                                               断言语句失败
        |   +- AttributeError                                               对象没有这个属性
        |   +- EnvironmentError                                             操作系统错误的基类
        |   |   +- IOError                                                  输入输出失败
        |   |   +- OSError                                                  操作系统错误
        |   |       +- WindowError (Windows)                                windows系统调用失败
        |   |       +- VMSError (VMS)
        |   +- EOFError                                                     没有内建输入，到达EOF标记
        |   +- ImportError                                                  导入模块/对象 失败
        |   +- LookupError                                                  无效数据查询的基类
        |   |   +- IndexError                                               序列中没有此索引 (index)
        |   |   +- KeyError                                                 映射中没有这个键
        |   +- MemoryError                                                  内存溢出错误（对于 Python 解释器不是致命的）
        |   +- NameError                                                    未声明/初始化对象（没有属性）
        |   |   +- UnboundLocalError                                        访问未初始化的本地变量
        |   +- SyntaxError                                                  Python 语法错误
        |   |   +- IndentationError                                         缩进错误
        |   |       TabError                                                Tab和空格混用
        |   +- SystemError                                                  一般的解释器系统错误
        |   +- TypeError                                                    对类型的无效操作
        |   +- ValueError                                                   传入无效的操作
        |       +- UnicodeError                                             Unicode 相关错误
        |           +- UnicodeDecodeError                                   Unicode 解码时错误
        |           +- UnicodeEncodeError                                   Unicode编码时错误
        |           +- UnicodeTransLateError                                Unicode转换时错误
        +- Warning                                                          警告的基类
            +- DeprecationWarning                                           关于被弃用的特征的警告
            +- PendingDeprecationWarning                                    关于构造将来语义会改变的警告
            +- RuntimeWarning                                               可疑的运行时行为的警告
            +- SyntaxWarning                                                可疑的语言的警告
            +- UserWarning                                                  用户代码生成警告
            +- FutureWarning
            +- ImportWarning                                                导入模块/对象警告
            +- UnicodeWarning                                               Unicode警告
            +- BytesWarning                                                 Bytes警告
                +- Overflow Warning                                        旧的关于自动提升为长整形（long）的警告


5. Built-in Exception
In Python, all exceptions must be instance of a class that derives from BaseException. In a try statement with an except
clause that mentions a particular class, that clause also handler any exception classes derived from that class (but
not exception classes from which it is derived). Two exception classes that are not related via subclassing are never
equivalent, even if they have the same name.

The built-in exceptions listed below can be generated by the interpreter or built-in functions. Except where mentioned,
they have an "associated value" indicating the detailed cause of the error. This may be a string or a tuple of several
items of information (e.g., an error code and a string explaining the code). The associated value is usually passes as
arguments to the exception class's constructor.

User code can raise built-in exceptions. This can be used to test an exception handler or to report an error condition "
just like" the situation in which the interpreter raises the same exception; but beware that there is nothing to prevent
user code from raising an inappropriate error.

The built-in exception classes can be subclasses to define new exception; programmers are encouraged to drive new
exceptions from the Exception class or one its subclasses, and not from BaseException. Morw information on defining
exceptions is available in the Python Tutorial under User-defined Exceptions.

When raising (or re-raising) an exception in an except or finally clause __context__ is automatically set to the last
exception caught; if the new exception is not handled the traceback that is eventually displayed will include the
originating exception(s) and the final exception.

When raising a new exception (rather than using a bare raise to re-raise )

5.1. Base classes

    exception BaseException
        args
        with_traceback(tb)
    exception Exception

    exception ArithmeticError

    exception BufferError

    exception LookupError

5.2. Concrete exceptions

    exception AssertionError

    exception AttributeError

    exception EOFError

    exception FloatingPointError

    exception GeneratorExit

    exception ImportError

    exception ModuleNotFoundError

    exception IndexError

    exception KeyError

    exception KeyboardInterrupt

    exception MemoryError

    exception NameError

    exception NotImplementedError

    exception OSError([arg])

    exception OSError([errno, strerror[, filename[, winerror[, filename2]]]])



"""