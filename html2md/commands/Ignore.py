from html2md.commands.Command import Command


class Ignore(Command):
    """
    Command that ignores the complete content of the tag this Command is assigned to.
    """

    def __init__(self, args):
        super().__init__()

    def __copy__(self):
        return Ignore(None)

    def execute(self) -> str:
        """
        Always returns an empty string
        :return: ""
        """
        return ""
