import re
from transformers.Tranformation import Transformation


def _sanitize(input_):
    if input_ == "\\n":
        return "\n"
    if input_ == "\\\\n":
        return "\\n"
    if input_ == "\\s":
        return "\\s"
    return input_


class LinkFixer(Transformation):

    def __init__(self, args):
        pass

    def execute(self, content: str) -> str:
        return re.sub('\\((?!.*http://)(.*)(.html)(#.*)?\\)', r'(\g<1>.md)', content)
