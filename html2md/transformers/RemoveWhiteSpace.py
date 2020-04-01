import re

from html2md.transformers.Tranformation import Transformation


class RemoveWhiteSpace(Transformation):

    def __init__(self, args):
        pass

    def execute(self, content: str) -> str:
        return re.sub(' +', ' ', content).replace("\n", "").replace("\r", "").replace("\t", "")
