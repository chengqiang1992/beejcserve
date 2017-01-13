"""
12. Virtual Environments and Packages
12.1 Introduction
Python applications will often use packages and modules that don't come as part of the standard library. Applications
will sometimes need a specific version of a library, because the application may require that a particular bug has been
fixed or the application may be written using an obsolete version of the library's interface.

The means it may not be possible for one Python installation to meet the requirements of every application. If application
A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict
and installing either version 1.0 or 2.0 will leave one application unable to run.

The solution for this problem is to create a virtual environment, a self-contained directory tree that contains a Python
installation for a particular version of Python, plus a number of additional packages.

Different applications can then use different virtual environments. To resolve the earlier example of conflicting
requirements, application A can haveits own virtual environment with version 1.0 installed while application B has
another virtual environment with version 2.0. If application B requires a library be upgraded to version 3.0, this will
not affect application A's environment.

12.2 Creating Virtual Environments
The module used to create and manage virtual environments is called venv. venv will usually install the most recent
version of Python that you have available. If you have multiple versions of Python on your system, you can select a
specific Python version by running Python3 or whichever version you want.
To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script
with the directory path:

python3 -m venv tutorial-env

This will create the tutorial-env directory if it doesn't exist, and also create directories inside it containing a copy
of the Python interpreter, the standard library, and various supporting files.

Once you've created a virtual environment, you may active it.

On windows, run:

tutorial-env\Scripts\activate.bat

Activating the virtual environment will change your shell's prompt to show what virtual  environment you're using, and
modify the environment so that running python will get you that particular version and installation of Python. For
example"

12.3 Managing Packages with pip
You can install, upgrade, and remove packages using a program called pip. By default pip will install packages from the
Python Package Index. You can browse the Python Package Index by going to it in your web browser, or you can use pip's
limited search feature:

pip has a number of subcommands: "search", "install", "uninstall", "freeze", tec

You can install the latest version of a package by specifying a package's name:

pip install novas

You can also install a specific version of a package by giving the package name followed by == and the version number

pip install request==2.6.0

If you re-run this command, pip will notice that the requested version is already installed and do nothing. You can
supply a different version number be get that version, or you can run pip install --upgrade to upgrade the package to
the latest version:

pip install --upgrade requests

pip uninstall followed by one or more package names will remove the packages from the virtual environment.

pip show will display informationabout a particular package.

pip list will display all the packages installed in the virtual environment

pip freeze will produce a similar list of the installed packages, but the output uses the format that pip install
expects. A common convention is to put this list in a requirement.txt file:

"""