import re

from html2md.commands.Command import Command


class Linearize(Command):
    """
    Command that linearizes the content of the tag.
    """

    def __init__(self, args):
        super().__init__()

    def __copy__(self):
        return Linearize(None)

    def execute(self) -> str:
        """
        Returns the content linearized
        :return: "The content without linebrakes"
        """
        return super().execute().replace("\\n", " ").strip()
