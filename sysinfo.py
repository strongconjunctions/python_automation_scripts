#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""System Information Gathering Script

"""

import subprocess
from sys import stdout


def uname():
    """uname command function"""
    print "\n\n"
    uname = "uname -a"

    printline1 = """
    \rGathering system information using `{0}` command\r
    """.format(uname).strip()
    print printline1
    for i in printline1:
        stdout.write("="),
    stdout.flush()
    print("\n")

    subprocess.call(uname, shell=True)
    print "\n\n"


def disk_space():
    """Function that runs the Unix 'df' command to measure
    disk space"""
    # Alternatively, you can split your command into command and separate
    # arguments
    df = "df"
    df_arg = "-h"
    printline2 = """
    \rGathering diskspace info using `{0} {1}` command\r
    """.format(df, df_arg).strip()
    print printline2
    for i in printline2:
        stdout.write("="),
    stdout.flush()
    print("\n")

    subprocess.call([df, df_arg])
    print "\n\n"


def temp_space():
    """This function will run shell command 'du -h' to measure the temp
    space on this machine"""
    du = "du"
    du_arg = "-h"
    temp = "/tmp"
    printline2 = """
    \rGathering diskspace used by the {2} dir using `{0} {1}` command\r
    """.format(du, du_arg, temp).strip()
    print printline2
    for i in printline2:
        stdout.write("="),
    stdout.flush()
    print("\n")

    subprocess.call([du, du_arg, temp])
    print "\n\n"


if __name__ == "__main__":
    uname()
    disk_space()
    temp_space()
