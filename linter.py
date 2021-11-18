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

class Norminette(Linter):
    """Provides an interface to norminette."""

    executable = 'norminette'

    regex = r'''(?xi)
        ^^(?:(?P<error>Error)|(?P<warning>Warning))   # Error
        # Norminette emits errors that pertain to the code as a whole,
        # in which case there is no line/col information, so that
        # part is optional.
        (?:(.+?(?P<line>\d+)))?
        (?:(.+?(?P<col>\d+)))?
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
            error["col"] = 1
        return error

    def reposition_match(self, line, col, m, vv):
        if col > 0:
            text = vv.select_line(line)
            col -= text[:col].count("\t") * 3
        return super().reposition_match(line, col, m, vv)

    def cmd(self):
        result = self.executable
        return result + ' ' + sublime.active_window().active_view().file_name()

