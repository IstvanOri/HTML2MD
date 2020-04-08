from html2md.commands.Indent import Indent
from html2md.commands.Command import Command
from html2md.commands.CommandConfigurationError import CommandConfigurationError


class IndentIn(Indent):
    """
    Command that levels an element based on the given string and the _level config value
    """

    def __init__(self, args):
        if len(args) < 2 or len(args) > 3:
            raise CommandConfigurationError("IndentIn("+",".join(args)+")", "IndentIn command takes two non-optional"
                                                                            "argument: the string to use as indent "
                                                                            "and the list of tags names to restrict "
                                                                            "indentation and an optional for first "
                                                                            "line indentation")
        if len(args) > 2:
            super().__init__((args[0], args[2]))
        else:
            super().__init__((args[0], ))
        self._tag_list: [str] = args[1].split(";")

    def __copy__(self):
        return IndentIn((self._indenting, ";".join(self._tag_list)))

    def execute(self) -> str:
        p: Command = self.ancestor
        while p is not None:
            if p.tag in self._tag_list:
                return super().execute()
            else:
                p = p.ancestor
        result = self.data
        for child in self._children:
            if result.find("[:child:]") > -1:
                result = result.replace("[:child:]", child.execute(), 1)
            else:
                result += child.execute()
        return result
