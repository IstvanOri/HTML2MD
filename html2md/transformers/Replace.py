from html2md.transformers.Tranformation import Transformation


def _sanitize(input_):
    if input_ == "\\n":
        return "\n"
    if input_ == "\\\\n":
        return "\\n"
    if input_ == "\\s":
        return "\\s"
    return input_


class Replace(Transformation):

    def __init__(self, args):
        self._from_ = _sanitize(args[0])
        self._to_ = _sanitize(args[1])

    def execute(self, content: str) -> str:
        return content.replace(self._from_, self._to_)
