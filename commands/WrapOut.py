from commands.Command import Command
from commands.Wrap import Wrap


class WrapOut(Wrap):

    def __init__(self, args):
        super().__init__((args[0], args[1], args[2]))
        self._tag_list: [str] = args[3].split(";")

    def __copy__(self):
        return WrapOut((self._prefix, self._suffix, self._allow_empty, ";".join(self._tag_list)))

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
