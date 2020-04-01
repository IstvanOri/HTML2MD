from html2md.commands.Command import Command
from html2md.commands.Wrap import Wrap


class WrapIn(Wrap):

    def __init__(self, args):
        super().__init__((args[0], args[1], args[2]))
        self._tag_list: [str] = args[3].split(";")

    def __copy__(self):
        return WrapIn((self._prefix, self._suffix, self._allow_empty, ";".join(self._tag_list)))

    def execute(self) -> str:
        p: Command = self.ancestor
        while p is not None:
            if p.tag in self._tag_list:
                return super().execute()
            else:
                p = p.ancestor
