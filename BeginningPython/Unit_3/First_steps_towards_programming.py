"""
Of course, we can use Python for more complicated tasks than adding two and two together. For instance,
 we can write an initial sub-sequence of the Fibonacci series as follows:
"""
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

'''
1: In Python, likes in C, any non-zero integer value is true; zero is false. In fact any sequence; anything
    with a non-zero length is true, empty sequence are false.
2: The body of the loop is indented: indentation is Python's way of grouping statements
'''
a, b = 0, 1
while b < 10:
    print(b, end=',')
    a, b = b, a+b


