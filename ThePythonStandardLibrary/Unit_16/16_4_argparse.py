'''
16.4 argparse -- Parser for conmand-line options, arguments and sub-commands
    16.4.1. Example
        16.4.1.1. Creating a parser
        16.4.1.2. Adding aruguments
        16.4.1.3. Parsing arguments
    16.4.2. ArgumentParser objects
        16.4.2.1 prog
        16.4.2.2. usage
        16.4.2.3. description
        16.4.2.4. epilog
        16.4.2.5. parents
        16.4.2.6. formatter_class
        16.4.2.7. prefix_chars
        16.4.2.8. fromfile_prefix_chars
        16.4.2.9. argument_deafault
        16.4.2.10. allow_abbrev
        16.4.2.11. conflict_handler
        16.4.2.12. add_helo
    16.4.3. The add_argument() method
        16.4.3.1. name or flags
        16.4.3.2. action
        16.4.3.3. nargs
        16.4.3.4. const
        16.4.3.5. default
        16.4.3.6. type
        16.4.3.7. choices
        16.4.3.8. required
        16.4.3.9. help
        16.4.3.10. metaver
        16.4.3.11. dest
        16.4.3.12. Action classes
    16.4.4. The parse_args() method()
        16.4.4.1. Option value syntax
        16.4.4.2. Invalid arguments
        16.4.4.3. Arguments containing-
        16.4.4.4. Argument abbreviations (prefix matching)
        16.4.4.5. Beyond sys.argv
        16.4.4.6. The Namespace object
    16.4.5. Other utilties
        16.4.5.1. Sun-commands
        16.4.5.2. FileType objects
        16.4.5.3. Argument groups
        16.4.5.4. Mutual exclusion
        16.4.5.5. Parser defaults
        16.4.5.6. Printing help
        16.4.5.7. Partial parsing
        16.4.5.8. Customizing file parsing
        16.4.5.9. Exiting methods
    16.4.6. Upgrading optparse code


    16.4. argparse -- Parser for command-line options, arguments and sub-commands

        The argparse module makes it easy to write user friendly command-line interfaces. To program defines what
        arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also
        automatically generates help and usage messages and issues errors when users give the program invalid arguments.

        16.4.1. Example
            The following code is a Python program that takes a list of integers and produces either the sum or the max:
            ____________________________________________________________________________________________________________
            import argparse
            parser = argparse.ArgumentParser(description='Process some integers.')
            parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
            parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,
                                help='sum the integers (default: find the max)')
            args = parser.parse_args()
            print(args.accumulate(args.integers))
            ------------------------------------------------------------------------------------------------------------

            Assuming the Python code above is saved into a file called prog.py, it can be run at the command line and
            provides useful help messages:
            _____________________________________________________________
            $ python prog.py -h
            usage: prog.py [-h] [--sum] N [N ...]

            Process some integers.

            positional arguments:
             N           an integer for the accumulator

            optional arguments:
             -h, --help  show this help message and exit
             --sum       sum the integers (default: find the max)
             -----------------------------------------------------------

             When run with the appropriate arguments, it prints either the sum of the max of the command-line integers:
             ________________________________
             $ python prog.py 1 2 3 4
             4

             $ python prog.py 1 2 3 4 --sum
             10
             -------------------------------

             if invalid arguments are passed in, it will issue an error:

             16.4.1.1. Creating a parser
                The first step in using the argparse is creating an ArgumentParser object:
                    >>> parser = argparse.ArgumentParser(description='Process some integers.')
                The ArgumentParser object will hold all the information necessary to parse the command line into Python
                data types.

             16.4.1.2. Adding arguments
                Filling an ArgumentParser with information about program is done by making calls to the add_argument() method.
                Generally, these calls tell the argumentParser how to take the string on the command line and turn them
                into objects. This information is stored and used when parse_args() is called. For example:
                ________________________________________________________________________________________________________
                parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
                parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,
                                    help='sum the integers (default: find the max)')
                --------------------------------------------------------------------------------------------------------
                Later, calling parse_args() will return an object with two attributes, integers and accmulate. The integers
                attribute will be a list of one or more ints, and the accumulate attribute will be either the sum()
                function, if --sum was specified at the command line, or the max() function if it was not.

            16.4.1.3. Parsing arguments

        16.4.2. ArgumentParser objects
            class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[],
            formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None,
            conflict_handler='error', add_help=True, allow_abbrev=True)

            Create a new ArgumentParser object. All parameters should be passed as keyword arguments. Each parameter has
            its own more description below, but in short they are:
                prog - The name of the program (default: sys.argv[0])
                usage - The string describing the program usage (default: generated from arguments added to parser)
                description - Text to display before the argument help (default: none)
                epilog - Text to display after the argument help (default: none)
                parents - A list of ArgumentParser objects whose arguments should also be included
                formatter_class - A class for customizing the help output
                prefix_chars - The set of characters that prefix optional arguments (default: ‘-‘)
                fromfile_prefix_chars - The set of characters that prefix files from which additional arguments should
                    be read (default: None)
                argument_default - The global default value for arguments (default: None)
                conflict_handler - The strategy for resolving conflicting optionals (usually unnecessary)
                add_help - Add a -h/--help option to the parser (default: True)
                allow_abbrev - Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True)

            16.4.2.1. prog参数
                默认情况下，ArgumentParser对象使用sys.argv[0]决定在帮助信息中如何显示程序的名字。这个默认值几乎总能满足
                需求，因为帮助信息（中的程序名称）会自动匹配命令行中调用的程序名称。例如，参考下面这段myprogram.py文件中
                的代码：

            16.4.2.2. usage参数
                默认情况下，ArgumentParser依据它包含的参数计算出帮助信息：

            16.4.2.3. description参数
                ArgumentParser构造器的大部分调用都将使用description=关键字参数。这个参数给出程序做什么以及如何工作的简短
                描述。在帮助信息中

            16.4.2.4. epilog参数
                有些程序员喜欢在参数的描述之后显示额外的关于程序的描述。这些文本可以使用ArgumentParser的epilog=参数制定：






































'''

