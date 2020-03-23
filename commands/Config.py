from commands.Command import Command
from commands.CommandConfigurationError import CommandConfigurationError


class Config(Command):
    """
    Command that overrides a specific config property.

    Currently supported configs:
        _bullet (default: ' * ')
    """

    def __init__(self, args):
        super().__init__()
        if len(args) != 2:
            raise CommandConfigurationError("Config("+",".join(args)+")", "Config command takes exactly two arguments: property name and value")
        self._attr = args[0]
        self._val = args[1]

    def __copy__(self):
        return Config((self._attr, self._val))

    def execute(self) -> str:
        """
        Overrides a given config property, runs the children and restores the property.
        :return: The result of the child Commands with the given Config
        """
        old = getattr(Command, self._attr)
        to_set = self._val
        if self._val == "++":
            to_set = int(old) + 1
        if self._val == "--":
            to_set = int(old) - 1
        setattr(Command, self._attr, to_set)
        result = super().execute()
        setattr(Command, self._attr, old)
        return result
