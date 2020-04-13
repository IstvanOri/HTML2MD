import re

from html2md.transformers.Tranformation import Transformation


def whitespace_escape(param: str):
    result = param.replace("\n", "\\n")
    result = result.replace("\t", "\\t")
    result = result.replace(" ", "\\s")
    return result


class RemoveWhiteSpace(Transformation):

    def __init__(self, args):
        pass

    def execute(self, content: str) -> str:
        result = re.sub("(<pre>|<code[^>]*>)(.*?)(</code>|</pre>)",
                        lambda m: m.group(1) + whitespace_escape(m.group(2)) + m.group(3),
                        content,
                        flags=re.DOTALL)
        result = re.sub(' +', ' ', result).replace("\n", "").replace("\r", "").replace("\t", "")
        return re.sub('> <', '><', result)
