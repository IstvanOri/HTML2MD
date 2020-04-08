from html2md.commands.Command import Command
from html2md.commands.CommandConfigurationError import CommandConfigurationError
from html2md.commands.VariableResolver import VariableResolver


class Wrap(Command):
    """
    Wraps the content of the tag this command is assigned to with the given prefix and suffix.
    """

    def __init__(self, args):
        super().__init__()
        if len(args) < 2 or len(args) > 3:
            raise CommandConfigurationError("Wrap("+",".join(args)+")", "Wrap command takes two arguments: prefix and "
                                                                        "suffix and an optional third argument "
                                                                        "allow_empty")
        self._prefix: str = args[0]
        self._suffix: str = args[1]
        self._allow_empty: bool = False
        if len(args) > 2:
            self._allow_empty = args[2] == "True"

    def __copy__(self):
        return Wrap((self._prefix, self._suffix, self._allow_empty))

    def execute(self) -> str:
        resolver = VariableResolver()
        prefix = resolver.resolve(self._prefix)
        suffix = resolver.resolve(self._suffix)
        content = super().execute()
        if len(content) > 0 and not content.isspace() or self._allow_empty:
            return prefix + content + suffix
        return ""
