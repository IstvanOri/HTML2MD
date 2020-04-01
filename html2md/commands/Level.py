from html2md.commands.Command import Command
from html2md.commands import CommandConfigurationError


class Level(Command):
    """
    Command that levels an element based on the given string and the _level config value
    """

    def __init__(self, args):
        super().__init__()
        if len(args) != 1:
            raise CommandConfigurationError("Level command takes exactly on argument: the string to use as leveling")
        self._leveling = args[0]

    def __copy__(self):
        return Level((self._leveling,))

    def execute(self) -> str:
        """
        Always returns an empty string
        :return: ""
        """
        indent = ""
        for i in range(1, self._level):
            indent += self._leveling
        result = ""
        for line in super().execute().split("\\n"):
            result += indent + line + "\\n"
        return result[:-2]
