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
from SublimeLinter.lint import Linter, persist
import sublime
import os
import string

class Norminette(Linter):
    """Provides an interface to norminette."""

    syntax = 'c'
    executable = 'norminette'

    regex = r'''(?xi)
        ^^(?:(?P<error>Error)|(?P<warning>Warning))   # Error
        # Norminette emits errors that pertain to the code as a whole,
        # in which case there is no line/col information, so that
        # part is optional.
        (?:(.+?(?P<line>\d+)))?
        (?:(.+?(?P<col>\d+)))?
        (?:(?P<message>.+))
    '''

    multiline = True
    error_stream = util.STREAM_BOTH
    selectors = {}
    defaults = {}

    def split_match(self, match):

        match, line, col, error, warning, message, near = super().split_match(match)

        if line is None and message:
            line = 0
            col = 0

        return match, line, col, error, warning, message, near

    def cmd(self):
        result = self.executable
        return result + ' ' + sublime.active_window().active_view().file_name()

