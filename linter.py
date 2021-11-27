#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Baptiste JAMIN
# Copyright (c) 2016 Baptiste JAMIN
#
# License: MIT
#

"""This module exports the 42Norminette plugin class."""

import shlex
from SublimeLinter.lint import Linter, persist, util
import sublime
import os
import string
import math

class Norminette(Linter):
    """Provides an interface to norminette."""
    cmd = "norminette ${file_on_disk}"

    tempfile_suffix = "-"

    regex = r'''(?xi)
        ^^(?:(?P<error>Error)|(?P<warning>Warning))   # Error
        # Norminette emits errors that pertain to the code as a whole,
        # in which case there is no line/col information, so that
        # part is optional.
        (?:(.+?(?P<line>\d+)))?
        (?:(.+?(?P<col2>\d+)))?
        (?:\)\:\s*)?
        (?:(?P<message>.+))
    '''
    
    line_col_base = (1, 1)
    multiline = True
    error_stream = util.STREAM_BOTH
    defaults = {
        'selector': 'source.c'
    }

    def split_match(self, match):
        error = super().split_match(match)
        if error["message"] and error["line"] is None:
            error["line"] = 1
            error["col2"] = 1
        error["col"] = int(error["col2"])
        return error

    def reposition_match(self, line, col, m, vv):
        col = int(m['col2'])
        if col > 0:
            content = vv.select_line(line)
            c = 0
            cr = 0
            maxc = col
            while c < maxc and c < len(content):
                if content[c] == '\t':
                    spaces = (4 - math.ceil(cr % 4))
                    col -= spaces
                    cr += spaces
                c += 1
                cr += 1

        return super().reposition_match(line, col, m, vv)
