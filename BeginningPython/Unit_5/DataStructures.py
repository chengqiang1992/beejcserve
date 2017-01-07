"""
5. Data Structures
    5.1 More on Lists
        5.1.1 Using Lists as Stacks
        5.1.2 Using Lists as Queues
        5.1.3 List Comprehensions
        5.1.4 Nested List Comprehensions'
    5.2 The del statement
    5.3 Tuples and Sequences
    5.4 Sets
    5.5 Dictionaries
    5.6 Looping Techniques
    5.7 More on Conditions
    5.8 Comparing Sequences and Other Types
"""


from collections import deque       # 列表模仿队列


"""
5. Data Structures
    5.1 More on Lists
        list.append(x)      Add an item to the end of the list. EQ to a[len(a):] = [x]
        list.extend(L)      Extend the list by appending all the items in the given list.
                            Equivalent to a[len(a):] = L
        list.insert(i,x)    insert an item at a given position. The first argument is the index
                            of the element before which to insert, so a,insert(0, x) insert at the front
                            of the list, and a.insert(len(a), x) is equivalent to a.append(x).
        list.remove(x)       remove the first item from the list whose value is x. It is error
                            if there is no such item.
        list.pop([i])       Remove the item at the given position in the list, and return it. if no index
                            is specified, a pop() removes and returns the last item in the list.
                            (The square brackets around the i in the method signature denote that the
                             parameter is optional, not that you should type square brackets at the position.
                             You will see this notation frequently in the Python Library Reference)
        list.clear()        remove all items from the list
        list.index(x[, start[, end]])   return zero-based index in the list of the first item whose value is x
        list.count(x)       Return the number of times x appears in the list
        list.sort(ket=None, reverse=False)  Sort the items of the list in place(the arguments can be
                            used for sort customization, see sorted() for their explanation)
        list.reverse()      reverse the elements of the list in place
        list.copy()         Return a shallow copy of the list
"""

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop())


"""
5.1.1 Using Lists as Stacks
The list methods make it very easy to use a list as a stack, where the last element added
is first element retrieved ("last-in, first-out"). To add an item to the top of the stack, use
append(), To retrieve an item from the top of the stack, use pop() without an explicit index.
"""
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack.pop())


"""
5.1.2 Using lists as Queues
It is also possible to use a list as a queue, where the first element added is the firs
element retrieved("first-in, first-out"); however, lists are not efficient for the purpose.
while appends and pops from the end of list are fast, doing insert or pops from the beginning
of a list is slow(because all of the other elements have to be shifted by one).
To implement a queue, use collection.deque which was designed to have fast appends and pops from
both ends. for example
"""

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)


"""
5.1.3 List Comprehensions
List comprehensions provide a concise way to create lists. Common applications are to make
new lists where each element is the result of some operations applied to each member of another
sequence or iterable, or to crate a subsequence of those elements that satisfy a certain condition
"""
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)


"""
5.1.4  Nested List Comprehensions
The initial expression in a list comprehensions can be any arbitrary expression, include
another list comprehension. Consider the following example of a 3×4 matrix implemented
as a list of 3 lists of length 4:
"""
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# The following list comprehensions will transport rows and columns:
print([[row[i] for row in matrix] for i in range(len(matrix[0]))])


"""
5.2 The del statement
There is a way to remove an item from a list given its index instead of its value: the del statement.
This differs from the pop() method which returns a value. The del statement can also be used to
remove slice from a list or clear the entire list (which we did earlier by assignment of an  empty)
list to the slice
"""
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
# del a
# print(a)      # Referencing the name a hereafter is an error (at least until another value is
# assigned to it). we'll find other users for del later.


"""
5.3 Tuples and Sequences
"""
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)                # Tuples may be nested
print(u)
# t[0] = 88888                        # Tuples are immutable
v = ([1, 2, 3], [3, 2, 1])            # but they can contain mutable objects
print(v)

"""
A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra
quirks to accommodate. Empty tuples are constructed by an empty pair of parentheses; a tuple with
one item is constructed by following a value with a comma(it is not sufficient to enclose a single
value in parentheses). ugly, but effective. For example:
"""
empty = ()
singleton = 'hello',
print(len(empty))
print(len(singleton))
# 所以，tuple所谓的不变是说，tuple的每个元素，指向永远不变。即指向'a'，就不能指向'b'，只想一个
# list, 就不能指向其他对象，但指向的这个list本身是可变的


"""
5.4 Sets
Python also includes a data type for sets. A set is an unordered collection with no duplicate
elements. Basic uses include membership testing and eliminating duplicate entries. Set objects
also mathematical operations like union, intersection, difference, and symmetric difference.

Curly braces or the set() function can be used to create sets. Note: to create an empty set
you have to use set(), not {}; the latter create an empty dictionary, a data structure that
we discuss in the next section.
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)


"""
5.5 Dictionaries
Another useful data type built into Python is the dictionary (see Mapping Types - dict). Dictionaries
are sometimes found in other languages as "associative memories" or "associative array". Unlike
sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be
any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they
contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly
or indirectly, it cannot be used as a key. You can't use lists as keys, since lists can be modified
in place using index assignments, slice assignments, or methods like append() and extend()

It is best to think of a dictionary as an unordered set of keys, with the requirement that the
keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}.
Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs
to the dictionary; this is also the way dictionaries are written are written on output.

The main operations on a dictionary are storing a value with some key and extracting the value
given the key. It is also possible to delete a key:value pair with del. If you store using a key that
already in use, the old value associated with that key is forgotten. It is an error to extract a value
using a non-existent key.
 """

"""
5.6  Looping Techniques
when looping through dictionaries, the key and corresponding value can be retrieved at the same
time using the items() method.
"""
knights = {'gallahad': 'the true', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, ': ', v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, ':', v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))


"""
5.8  Comparing Sequences and Other Types
Sequence objects may be compared to other objects with the same sequence type. The comparison
uses lexicographical ordering: first the first two items are compared, and if they differ this
determines the outcome of the comparison; if they are equal, the next two items are compared,
and so on, until either sequence is exhausted. if two items to be compared are themselves sequences
of the same,

Lexicographical ordering for string uses the Unicode point number to order individual characters.
some examples of comparisons between sequences of the same type:
"""
print((1, 2, 3) < (1, 2, 4))
print([1, 2, 4] < [1, 2, 3])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4) < (1, 2, 4))
print((1, 2, 3) == (1.0, 2.0, 3.0))

























































