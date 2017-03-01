"""
11.2. os.path --- Common pathname manipulations

    This module implements some useful functions on pathnames. To read or write files see open(), and for accessing the
    filesystem see the os module. The path parameters can be passed as either strings, or bytes. Applications are
    encouraged to represent file names as (Unicode) character strings. Unfortunately, some file names may not be
    representable as strings on Unix, so applications that need to support arbitrary file names on Unix should use bytes
    objects to represent path names. Vice versa, using bytes objects cannot represent all file names on Windows(in the
    standard mbcs encoding), hence Windows applications should use string objects to access all files.

    Unlike a unix shell, Python does not do any automatic path expansions. Functions such as expanduser() and
    expandvars() can be invoked explicatly when an application desires shell-like path expansion. (See also the glob
    module)

    os.path.abspath(path)
        Return a normalized absolutized version of the pathname path. On most platforms, this is equivalent to calling
        the function normpath() as follows: normpath(join(os.getcwd(), path)).
            import os
            print("1:" + os.path.abspath('ospath.py'))
            print("2:" + os.path.normpath('ospath.py'))
            print("3:" + os.path.normpath(os.getcwd()))

    os.path.basename(path)
        Return the base name of pathname path. This is the second element of the pair returned by passing path to the
        function split(). Note that the result of this function is different from the Unix basename program; where
        basename for '/foo/bar' returns 'bar', the basename() functions returns any empty string('').
            print("1:" + os.path.basename('ospath.py'))
            print("2:" + os.path.basename('ospath.py'))
            print("3:" + os.path.basename(os.getcwd()))
"""


import os
print("1:" + os.path.abspath('ospath.py'))
print("2:" + os.path.normpath('ospath.py'))
print("3:" + os.path.normpath(os.getcwd()))

print("1:" + os.path.basename('ospath.py'))
print("2:" + os.path.basename('ospath.py'))
print("3:" + os.path.basename(os.getcwd()))

print("1:" + os.path.commonpath('ospath.py'))
print("2:" + os.path.commonpath('ospath.py'))

print("1:" + os.path.dirname(os.getcwd()))

print(os.path.exists("D:\BackEnd\LearnPython\ThePythonStandardLibrary"))
print(os.path.exists(os.getcwd()))

print(os.path.dirname(__file__))
print(os.path.exists(os.getcwd()))
