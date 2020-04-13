from html2md.commands.Command import Command
from html2md.commands.Wrap import Wrap


class WrapOut(Wrap):

    def __init__(self, args):
        super().__init__((args[0], args[1], args[2], args[3]))
        self._tag_list: [str] = args[4].split(";")

    def __copy__(self):
        return WrapOut((self._prefix, self._suffix, str(self._allow_empty), str(self._line_by_line), ";".join(self._tag_list)))

    def execute(self) -> str:
        p: Command = self.ancestor
        in_ = False
        while p is not None:
            if p.tag in self._tag_list:
                in_ = True
            p = p.ancestor
        if not in_:
            return super().execute()
        else:
            result = self.data
            for child in self._children:
                if result.find("[:child:]") > -1:
                    result = result.replace("[:child:]", child.execute(), 1)
                else:
                    result += child.execute()
            return result
