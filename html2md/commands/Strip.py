from html2md.commands.Command import Command


class Strip(Command):
    """
    Command that removes every trailing whitespace line-by-line
    """

    def __init__(self, args):
        super().__init__()

    def __copy__(self):
        return Strip(None)

    def execute(self) -> str:
        """
        The content of the tag and its children without any trailing whitespace
        :return: the stripped content
        """
        result: str = ""
        for lines in (super().execute()).splitlines():
            result += lines.strip()
        return result
