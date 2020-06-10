import re
from builtins import print

from slugify import slugify

from html2md.transformers.Tranformation import Transformation


class Slugify(Transformation):
    """
    Transformation that calls Slugify (https://pypi.org/project/python-slugify/) on a substring of the target that
    surrounded with a prefix given in the first argument and a suffix specified in the second argument.
    """

    def __init__(self, args):
        self._prefix_ = args[0]
        self._suffix_ = args[1]

    def execute(self, content: str) -> str:
        result = content
        links = re.compile(r'({})(.*)({})'.format(self._prefix_, self._suffix_))
        result = re.sub(links, lambda m: m.group(1)+slugify(m.group(2))+m.group(3), result)
        return result
