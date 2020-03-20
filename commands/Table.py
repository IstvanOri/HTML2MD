from commands.Command import Command
import re


class Table(Command):
    """
        Constructs a table. The header will be the first row of the children
    """

    def __init__(self, args):
        super().__init__()
        self._prefix: str = args[0]
        self._suffix: str = args[1]

    def __copy__(self):
        return Table((self._prefix, self._suffix))

    def execute(self) -> str:
        """
        Creates an MD table.
        :return: an MD table
        """
        result: str = ""
        first: bool = True
        for child in self._children:
            result += child.execute()
            if first:
                first = False
                result += "---"+"---".join(re.sub('[^|]',"",result))
                result += "\\n"
        return self._prefix + result + self._suffix
