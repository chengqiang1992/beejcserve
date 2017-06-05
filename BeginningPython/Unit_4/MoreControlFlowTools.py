"""
4. 深入 Python 流程控制
    除了前面介绍的while语句，python 还从其他语言借鉴了一些流程控制功能，并有所改变。
    4.1. if 语句
        也许最有名的就是 if 语句。例如
"""
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")
"""
        可能会有零到多个elif部分，else是可选的。关键字'elif'是else if的缩写，这个可以有效地避免过深的缩进。if...elif...elif...
        序列用于替代其他语言中的 switch 或 case 语句。
"""


"""
    4.2. for 语句
        Python 中的 for 语句和 C 或 Pascal 中的略有不同。通常的循环可能会依据一个等值数值步进过程（如 Pascal），或由用户来定义
        迭代步骤和终止条件（如 C），Python 的 for 语句依据任意序列（链表或字符串）中的子项，按他们在序列中的序列中的顺序来迭代。
        例如（没有暗指）
"""
words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))
"""
        在迭代过程中修改迭代序列不安全（只有在使用链表这样的可变序列时才会有这样的情况）。如果你想要修改你迭代的序列（例如，复制
        选择项），你可以迭代他的副本。使用切个标识就可以很方便的做到这一点：
"""
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)


"""
    4.3. range() 函数
        如果你需要一个数值序列，内置函数 range() 会很方便，他声称一个等差级数链表：
"""
for i in range(5):
    print(i)
"""
        range(10) 生成一个包含 10 个值得链表，它用链表的索引值填充了这个长度为10的列表，所生成的链表中不包括范围中的结束值。
        也可以让range() 操作从另一个数值开始，或者可以指定一个不同的步进值（甚至是负数，有时这也被成为"步长"）
"""
range(5, 10)

range(0, 10, 3)

range(-10, -100, -30)
"""                                                         
需奥迭代链表索引的话，如下所示结合使用 range() 和 len()         enumerate(iterable, start=0) Return an enumerate object
"""
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))

# Equivalent to:

def enumerate(sequence, start = 0):
    n = start
    for elem in sequence:
        yield n, elem
        n + 1
"""
在不同方面 range() 函数返回的对象表现为它是一个列表，但事实上它并不是。当你迭代它时，它是一个能够像期望的序列返回连续项的对象；
但为了节省空间，它并不真正构造列表。

我们称此类对象是可迭代的，即适合作为那些期望从某些东西中获得连续项直到结束的函数或结构的一个目标(参数)。我们已经见过的for语句
就是这样一个迭代器。list() 函数是另外一个(迭代器)，他从可迭代(对象)中创建列表：
"""
list(range(5))  # [0, 1, 2, 3, 4]

