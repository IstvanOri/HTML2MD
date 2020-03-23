from pprint import pprint

from commands.Command import Command
from commands.CommandConfigurationError import CommandConfigurationError


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
        result = ""
        for i in range(1, self._level):
            result += self._leveling
        return result + super().execute()
