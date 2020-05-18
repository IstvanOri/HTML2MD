import re

from html2md.transformers.Tranformation import Transformation


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
        local_links = re.compile(r'\((?!\s*http)([^\[\]]*)(\.html)(.*)\)')
        result = re.sub(local_links, r'(\g<1>.md\g<3>)', content)
        return result
