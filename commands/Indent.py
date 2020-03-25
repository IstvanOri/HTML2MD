from commands.Command import Command
from commands.CommandConfigurationError import CommandConfigurationError


class Indent(Command):
    """
    Command that Indents an element based on the given string
    """

    def __init__(self, args):
        super().__init__()
        if len(args) != 1:
            raise CommandConfigurationError("Indent command takes exactly on argument: the string to use as Indenting")
        self._indenting = args[0]

    def __copy__(self):
        return Indent((self._indenting,))

    def execute(self) -> str:
        result = ""
        for line in super().execute().split("\\n"):
            result += self._indenting + line + "\\n"
        return result[:-2]