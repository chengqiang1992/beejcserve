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
'''