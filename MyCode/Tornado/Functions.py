# 第七章：函数

# 为了能让一个函数接受任意数量的位置参数，可以使用一个 * 参数。 例如：


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

avg(1, 2)
print(avg(1, 2))
avg(1, 2, 3, 4)
print(avg(1, 2, 3, 4))

# 为了能让一个函数接受任意数量的关键字参数，使用一个以 ** 开头的参数。 例如：


import html


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    print(attr_str)
    element =  '<{name}{attrs}>{value}</{name}>'.format(
        name = name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element

# Example
# Create '<item size="large" quantity="6">Albatross</item>'
make_element('item', 'Albatross', size="large", quantity=6)
print(make_element('item', 'Albatross', size="large", quantity=6))

"""
如果你还希望某个函数能同时接受任意数量的位置参数和关键字参数，可以同时使用 * 和 **。比如：

    def anyargs(*args, **kwargs):
        print(args)     # A tuple
        print(kwargs)   # A dict


讨论
    一个 * 参数只能出现在函数定义中最后一个位置参数后面，而 ** 参数只能出现在最后一个参数。有一点要注意的是，
    在 * 参数后面仍然可以定义其他参数：
        def a(x, *args, y):
        pass

        def b(x, *args, y, **kwargs):
            pass

"""

"""
7.10 带额外状态信息的回调函数

问题
    你的代码中需要依赖到回调函数的使用（比如事件处理器、等待后台任务完成后的回调等），并且你还需要让回调函数
    拥有额外的状态值，以便在它的内部使用到。

解决方案
    这一小节主要讨论的是那些出现在很多函数库和框架中的回调函数的使用 -- 特别是跟异步处理有关的。为了演示与测试
    我们先定义如下一个需要调用回调函数的函数：
        def apply_async(func, args, *, callback):
            # Compute the result
            result = func(*args)

            # Invoke the callback with the result
            callback(result)
    实际上，这段代码可以做任何更高级的处理，包括线程、进程和定时器，但是这些都不是我们要关心的。我们仅仅只需要
    关注回调函数的调用。下面是一个演示怎样使用上述代码的例子：
        def print_result(result):
            print('Got:', result)


        def add(x, y):
            return x + y

        apply_async(add, (2, 3), callback=print_result)
        apply_async(add, ('hello', 'world'), callback=print_result)

    注意到 print_result() 函数仅仅只接受一个参数 result。不能再传入其他信息。而当你想让回调函数访问其他变量
    或者特定环境的变量值的时候就会遇到麻烦。

    为了让回调函数访问外部信息，一种方法是使用一个绑定方法来代替一个简单函数。比如，下面这个类会保存一个内部序
    列号，每次接收到 result 的时候序列号加1：
        class ResultHandler:
            def __init__(self):
                self.sequence = 0

            def handler(self, result):
                self.sequence += 1
                print('[{}] Got: {}'.format(self.sequence, result))

    第二种方式，作为类的替代，可以使用一个闭包捕获状态值，例如：
        def make_handler():
            sequence = 0

            def handler(result):
                nonlocal sequence
                sequence += 1
                print('[{}] Got: {}'.format(sequence, result))
            return handler
    下面是使用闭包方式的一个例子：
        handler = make_handler()
        apply_async(add, (2, 3), callback=handler)
        apply_async(add, ('hello', 'world'), callback=handler)



"""


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence   #nonlocal 声明语句用来指示接下来的变量会在回调函数中被修改。如果没有这个声明，代码会报错。
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler


def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


# apply_async(add, (2, 3), callback=print_result)
# apply_async(add, ('hello', 'world'), callback=print_result)
# r = ResultHandler()
# apply_async(add, (2, 3), callback=r.handler)
# apply_async(add, ('hello', 'world'), callback=r.handler)

# handler = make_handler()
# apply_async(add, (2, 3), callback=handler)
# apply_async(add, ('hello', 'world'), callback=handler)

handler = make_handler()
next(handler)   # Advance to the yield
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, ('hello', 'world'), callback=handler.send)




