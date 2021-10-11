# -*- coding: utf-8 -*-
"""
Writable String Object | Stores data to simplify writing outputs.
Created on Sat Nov 28 19:06:09 2020

Version 1.3.0 (debug support) A-05-2021 @ 14:34 UTC -5
Requires: NONE

@author: Kinetos#6935
"""
import argparse


class wso(object):
    """
    A class to to simplify writing outputs when printing.

    Attributes
    ----------
    template : str
        Template used to format the printing string.
    outfile : str
        Path to the text file used for writing.
    writeable : bool
        Whether the write methods should write to a file when called.
    string : str
        Current formatted string to write or print.

    Methods
    -------
    fm(*args):
        Format the template string using *args. Stores result in self.string.
    wp():
        Write to file and print the currently stored string.
    p():
        Print the currently stored string.
    w():
        Write the currently stored string to the outfile.
    clean():
        Open the outfile with 'w' setting to clear any existing contents.

    """

    def __init__(self, template="", outfile="out.txt", debug=False):
        self.template = template
        self.outfile = outfile
        self.writeable = self.outfile is not None
        self.debug = debug
        self.string = ""

    def set_template(self, template):
        """
        Setter for template.

        Parameters
        ----------
        template : str
            Template used to format the printing string.

        Returns
        -------
        None.

        """
        self.template = template

    def set_outfile(self, filepath):
        """
        Setter for outfile.

        Parameters
        ----------
        filepath : str
            New path to text file to use for writing.

        Returns
        -------
        None.

        """
        self.outfile = filepath

    def set_writeable(self, writeable):
        """
        Setter for writeable.

        Parameters
        ----------
        writeable : bool
            Whether the write methods should write to a file when called.

        Returns
        -------
        None.

        """
        self.writeable = bool(writeable)

    def set_string(self, string):
        """
        Setter for string.

        Parameters
        ----------
        string : str
            New formatted string to write or print.

        Returns
        -------
        None.

        """
        self.string = string

    def get_template(self):
        """
        Getter for template.

        Returns
        -------
        template : str
            Template used to format the printing string.

        """
        return self.template

    def get_outfile(self):
        """
        Getter for outfile.

        Returns
        -------
        outfile : str
            Path to the text file used for writing.

        """
        return self.outfile

    def get_string(self):
        """
        Getter for string.

        Returns
        -------
        string : str
            Current formatted string to write or print.

        """
        return self.string

    def fm(self, *args):
        """
        Format the template string using *args. Stores result in self.string.

        Parameters
        ----------
        *args : object
            Values given as inputs for str.format().

        Returns
        -------
        None.

        """
        self.string = self.template.format(*args)

    def wp(self):
        """
        Write to file and print the currently stored string.

        Returns
        -------
        None.

        """
        if self.writeable:
            with open(self.outfile, 'a') as f:
                f.write(self.string + '\n')
        print(self.string)

    def p(self):
        """
        Print the currently stored string.

        Returns
        -------
        None.

        """
        print(self.string)

    def w(self):
        """
        Write the currently stored string to the outfile.

        Returns
        -------
        None.

        """
        if self.writeable:
            with open(self.outfile, 'a') as f:
                f.write(self.string)

    def clean(self):
        """
        Open the outfile with 'w' setting to clear any existing contents.

        Returns
        -------
        None.

        """
        if self.writeable:
            open(self.outfile, 'w').close()

    def fmwp(self, *args):
        """
        Perform fm() followed by wp().

        Parameters
        ----------
        *args : object
            Values given as inputs for str.format().

        Returns
        -------
        None.

        """
        self.fm(*args)
        self.wp()
    
    
    def dbwp(self, *args):
        """
        If debug mode is enabled, perform fm() followed by wp().

        Parameters
        ----------
        *args : object
            Values given as inputs for str.format().

        Returns
        -------
        None.

        """
        if self.debug:
            self.fm(*args)
            self.wp()


def generate_outfile_parser(description):
    """
    Reusable -o and -O arguments.

    Parameters
    ----------
    description : str
        Description for the argument parser, usually __doc__ or some variant.

    Returns
    -------
    p : argparse.ArgumentParser
        Created ArgumentParser object with -o, -O, and the given description.

    """
    p = argparse.ArgumentParser(description)
    p.add_argument("-o", "--outfile", dest="o", action="store_true",
                   help="output printed results to default file: out.txt")
    p.add_argument("-O", dest="oname", metavar="NAME",
                   help="output printed results to text file w/ custom path")
    return p


def implement_outfile_parser(args):
    """
    Implement -o and -O arguments added by generate_outfile_parser.

    Parameters
    ----------
    args : argparse args object
        Results of parse_args() when called on an Argument Parser object.

    Returns
    -------
    outfile : str, None
        None if neither args.oname nor args.o was set, do not output to file.

    Notes
    -----
    Use for docstring in methods that accept outfile as an argument:
    outfile : str, None
        Path to output text file. Disables writing to file if set to None.

    """
    outfile = None
    if args.oname is not None:
        outfile = args.oname.strip()
        if not outfile.endswith(".txt"):
            outfile += ".txt"
    elif args.o:
        outfile = "out.txt"
    return outfile


def init(template="", o=None, d=False):
    if o is not None:
        return wso(template, o, d)
    else:
        return wso(template, o, d)
