# # more controls flow tools
#
# # 4.1 if statements
# x = int(input("please enter an integer: "))
# if x < 0:
#     x = 0
#     print("Negative changed to zero")
# elif x == 0:
#     print("Zero")
# elif x == 1:
#     print("Signal")
# else:
#     print("more")
#
# # 4.2 for statements
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))
#
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])
#
# # 4.4 break and continue statements, and else clauses on loos
#
# '''
# 4.5 pass Statement
# The pass statement does nothing. It can be used when a statement is required, syntactically but the
# program requires no action. For example:
# '''
# # while True:
# #     pass            # Busy-wait for the keyboard interrupt (Ctrl + C)
#
# # class MyEmptyClass:
# #     pass
# #
# # def initlog(*args):
# #     pass
#
# # 4.6 Defining Functions
#
#
# def fib(n):             # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
#
# fib(2000)
# print(fib.__doc__)
#
#
# def fib2(n):            # return Fibonacci series up to n
#     """Return a list containing the Fibonacci series up to n"""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result
#
# print(fib2(100))
#
#
# # 4.7 More on Defining Functions
# # It is also possible to define functions with a variable number of arguments. There are three forms
# # which can be combined.
#
# # 4.7.1 Default Argument Values
# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
#
# print(ask_ok('Do you really want to quit?'))
# print(ask_ok('OK to overwrite the file?', 2))
# print(ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!'))
#
#
# def f(a, L=[]):
#     L.append(a)
#     return L
#
# print(f(1))
# print(f(2))
# print(f(3))

#
# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
#
# print(f(1))
# print(f(2))
# print(f(3))

# 4.7.2 Keyword Arguments
# Functions can also be called using keyword arguments of the form kwarg=value. For instance, the following function:


# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("--It's", state, "!")
#
# print(parrot(1000))                                             # 1 positional argument
# print(parrot(voltage=1000))                                     # 1 keyword argument
# print(parrot(voltage=100000, action='VOOOOOM'))                 # 2 keyword argument
# print(parrot(action="VOOOOOM", voltage=100000))                 # 2 keyword argument
# print(parrot('a million', 'bereft of life', 'jump'))            # 3 positional argument
# print(parrot('a thousand', state='pushing up the daisies'))     # 1 positional, 1 positional
#
# parrot()                                                        # required argument missing
# parrot(voltage=5.0, 'dead')                                     # 系统报错是 Positional argument after
#                                                                 # keyword argument
# parrot(110, voltage=220)                                        # duplicate value for the same argument
# parrot(actor='John Cleese')                                     # unknown keyword argument

"""
1. In a function call, keyword arguments must follow positional arguments.
2. All the keyword arguments passed must match one of the arguments accepted by the function
3. This also includes non-optional arguments (e.g. parrot(voltage=1000) is valid too).
4. No arguments may receive a value more than once
"""

"""
When a final formal parameter of the form **name is present, it receives a dictionary containing all keyword
arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter
 of the form *name which receives a tuple containing the positional arguments beyond the formal parameter list
"""


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           cliet="John Cleese",
           sketch="Cheese shop sketch")

"""
Finally, the least frequently used option is to specify that a function can be called with an arbitrary
number of arguments. These arguments will be wrapped up in a tuple. Before the variable number of arguments,
zero or more normal arguments many occur.
"""





