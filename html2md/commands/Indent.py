from html2md.commands.Command import Command
from html2md.commands.CommandConfigurationError import CommandConfigurationError


class Indent(Command):
    """
    Command that Indents an element based on the given string
    """

    def __init__(self, args):
        super().__init__()
        if len(args) < 1 or len(args) > 2:
            raise CommandConfigurationError("Indent("+",".join(args)+")", "Indent command takes one non-optional "
                                                                          "argument the string to use as Indenting "
                                                                          "and an optional to set behaviour for "
                                                                          "first line")
        self._indenting = args[0]
        self._is_first_line_indents: bool = True
        if len(args) == 2:
            self._is_first_line_indents = args[1] == "True"

    def __copy__(self):
        return Indent((self._indenting, self._is_first_line_indents))

    def execute(self) -> str:
        result = ""
        is_indenting = self._is_first_line_indents
        for line in super().execute().split("\\n"):
            if is_indenting:
                result += self._indenting
            result += line + "\\n"
            is_indenting = True
        return result[:-2]
