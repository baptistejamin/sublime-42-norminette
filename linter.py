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

    regex = (
        r'^(?:(?P<error>Error)|(?P<warning>Warning))'
        r'.+?line (?P<line>\d+)+?'
        r'(?P<message>.+)'
    )

    multiline = True
    error_stream = util.STREAM_BOTH
    selectors = {}
    defaults = {}

    def cmd(self):
        result = self.executable
        return result + ' ' + sublime.active_window().active_view().file_name()

