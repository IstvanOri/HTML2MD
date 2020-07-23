import re
from builtins import print

from slugify import slugify

from html2md.transformers.Tranformation import Transformation


class Slugify(Transformation):
    """
    Transformation that calls Slugify (https://pypi.org/project/python-slugify/) on a substring of the target that
    surrounded with a prefix given in the first argument and a suffix specified in the second argument.An optional
    3rd argument also can be passed which is a pattern the subject has to match.
    """

    def __init__(self, args):
        self._prefix_ = args[0]
        self._suffix_ = args[1]
        self._separator_ = args[2]
        self._pattern_ = ".+"
        if len(args) > 3:
            self._pattern_ = args[3]
        self._split_ = "\n"
        if len(args) > 4:
            self._split_ = args[4]

    def execute(self, content: str) -> str:
        result = ""
        links = re.compile(r'({})({})({})'.format(self._prefix_, self._pattern_, self._suffix_))
        first = True
        for part in content.split(self._split_):
            if not first:
                result += self._split_
            first = False
            result += re.sub(links, lambda m: m.group(1)+slugify(m.group(2), regex_pattern=self._separator_)+m.group(3), part)
        return result
