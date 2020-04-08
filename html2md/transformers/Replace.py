import re

from html2md.transformers.Tranformation import Transformation


class Replace(Transformation):

    def __init__(self, args):
        self._from_ = args[0]
        self._to_ = args[1]

    def execute(self, content: str) -> str:
        return re.sub(re.compile(self._from_), self._to_, content)
