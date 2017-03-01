"""
1. 介绍
Python 库是由几种不同类型的组成部分构成的。

包括组成一个编程语言最核心部分的数据类型，不如数字、列表。对于这些数据类型，Python语言核心定义了他们的表达形式和一些
语言规范，但并没有定义全部的语义。（比如，语言核心定义了语言规范，像拼写计算符的优先级。）

Python库还包括了内置函数和表达式，你可以在所有的Python代码中使用这些内置函数和表达式而不需要使用import语句。一些内置函数
和表达式是被Python本身核心代码所使用的，但是很多并不是核心语义所必须的，他们的存在只是为了方便使用。

Python库的主要由很多模块构成的。我们可以从很多方面去剖析这些模块。一些模块使用C语言携程并且内置到Python解析器中；另外的
是有Python编写并且以源代码的形式直接导入到Python中。一些模块提供非常具体的针对Python的接口，比如Python堆栈跟踪的模块；
一些是针对操作系统的，比如操作具体的硬件；还有一些模块提供某一应用领域的接口，比如面向互联网。一些模块可以在任意版本和
平台的Python中使用。另外游戏额只能在特定的系统支持的情况下才能使用；还有一些模块只有在便宜Python时使用了某些特定参数的
情况下才能使用。

本手册是按照“由内而外”的顺序组织的：首先介绍了内置数据结构，然后是内置函数和异常，最后分别在各个章节介绍相关的各种
模型。这些章节的是按照相关内容的重要程度由重要到不重要的顺序排序的。

这就意味着，不管你是从头阅读，还是因为无聊随便翻到某一章节，你都可以获得一个对于当前章节所讲解的模块以及其应用的合理的、
全面的了解。当然，你完全不必像阅读一部小说一样月u的这不手册，你可以查阅目录，或者直接在索引中搜索具体的函数、模块、条目。
最后，如果你希望学习随机的章节，你可以选择一个随机页面书（模块random）然后随便阅读一两节。不论你是按照什么顺序阅读手册的
各个部分，最好先阅读内置函数这张。

1. Introduction
The "Python library"  contains several different kinds of components.

It contains data types that would normally be considered part of the "core" of a language, such as numbers and lists.
For these types, the Python language core defines the form of literals and places some constraints on their semantics,
but does not fully define the semantics. (On the other hand, the language core does define syntactic properties like
the spelling and priorities of operator.)

The library also contains built-in function and exceptions - objects that can be used by all Python code without the
need of an import statement. Some of these are defined by the core language, but many are not essential for the core
semantics and are only described here.

The bulk of the library, however, consists of a collection of modules. There are many ways to dissect this collection.
Some modules are written in C and built in to the Python interpreter; other are written in Python and imported in
source form.
"""