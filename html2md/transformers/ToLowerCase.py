import re
from builtins import print

from html2md.transformers.Tranformation import Transformation


class ToLowerCase(Transformation):
    """
    Transformation that makes lowercase a substring of the target that surrounded with a prefix given in the first
    argument and a suffix specified in the second argument. An optional 3rd argument also can be passed which is a
    pattern the subject has to match.
    """

    def __init__(self, args):
        self._prefix_ = args[0]
        self._suffix_ = args[1]
        self._pattern_ = ".+"
        if len(args) > 2:
            self._pattern_ = args[2]

    def execute(self, content: str) -> str:
        result = content
        links = re.compile(r'({})({})({})'.format(self._prefix_, self._pattern_, self._suffix_))
        result = re.sub(links, lambda m: m.group(1)+m.group(2).lower()+m.group(3), result)
        return result
