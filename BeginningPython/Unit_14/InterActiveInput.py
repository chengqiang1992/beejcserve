"""
14. Interactive Input Editing and History Substitution
Some version of the Python interpreter support editing of the current input and history substitution, similar to
facilities found in the Korn shell and the GNU Bash shell. This is implemented using the GNU Readline library, which
supports various style of ending. This library has its own documentation which we won't duplicate here.

14.1 Tab Completion and History Editing
Completion of variable and module names is automatically enabled at interpreter startup so that the Tab key invoke the
completion function; it looks at Python statement names, the current local variables, and then available module names.
For dotted expression such as string.a, it will evaluate the expression up to the final '.' and then suggest completions
from the attributes of the resulting object. Note that this may execute application-defined code if an object
"""