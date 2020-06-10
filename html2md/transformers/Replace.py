import re
from builtins import print

from html2md.transformers.Tranformation import Transformation


class Replace(Transformation):
    """
    Transformation that replaces all occurrences of a string give in the first argument to another one given in the
    second argument. This Transformation accepts an optional third argument, if a line matches that argument the
    replacing is disabled until another matching line found.
    """

    def __init__(self, args):
        self._from_ = args[0]
        self._to_ = args[1]
        self._toggle_ = None
        if len(args) > 2:
            self._toggle_ = args[2]

    def execute(self, content: str) -> str:
        result = ""
        toggled = True
        for line in content.splitlines(True):
            if line.strip() == self._toggle_:
                toggled = not toggled
            if toggled:
                result += re.sub(re.compile(self._from_), self._to_, line)
            else:
                result += line
        return result
