from html2md.commands.Command import Command
from html2md.commands.CommandConfigurationError import CommandConfigurationError
from html2md.commands.VariableResolver import VariableResolver


class Wrap(Command):
    """
    Wraps the content of the tag this command is assigned to with the given prefix and suffix.
    """

    def __init__(self, args):
        super().__init__()
        if len(args) < 2 or len(args) > 4:
            raise CommandConfigurationError("Wrap("+",".join(args)+")", "Wrap command takes two arguments: prefix and "
                                                                        "suffix and an optional third and fourth "
                                                                        "argument for allow_empty and line-by-line "
                                                                        "wrap")
        self._prefix: str = args[0]
        self._suffix: str = args[1]
        self._allow_empty: bool = False
        if len(args) > 2:
            self._allow_empty = args[2] == "True"
        self._line_by_line: bool = False
        if len(args) > 3:
            self._line_by_line = args[3] == "True"

    def __copy__(self):
        return Wrap((self._prefix, self._suffix, str(self._allow_empty), str(self._line_by_line)))

    def execute(self) -> str:
        resolver = VariableResolver()
        prefix = resolver.resolve(self._prefix)
        suffix = resolver.resolve(self._suffix)
        content = super().execute()
        result = ""
        if (len(content) > 0 and not content.isspace()) or self._allow_empty:
            if self._line_by_line:
                for line in content.split("\\n"):
                    if (len(line) > 0 and not line.isspace()) or self._allow_empty:
                        result += prefix + line + suffix + "\\n"
                result = result[:-2]
            else:
                result = prefix + content + suffix
        return result
