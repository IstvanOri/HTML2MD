from html2md.commands.Command import Command
import re

from html2md.commands.TableBuffer import TableBuffer


class Table(Command):
    """
        Constructs a table. The header will be the first row of the children
    """

    CONTENT_BUFFER = TableBuffer()

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
        for child in self._children:
            child.execute()
        result += Command._table_cell_separator.join(self.CONTENT_BUFFER.rows[0])
        result += "\\n"
        row_sep = [Command._table_head_separator] * len(self.CONTENT_BUFFER.rows[0])
        result += Command._table_cell_separator.join(row_sep)
        result += "\\n"
        for row in self.CONTENT_BUFFER.rows[1:]:
            for i in range(len(row), len(self.CONTENT_BUFFER.rows[0])):
                row.reverse()
                row.append("")
                row.reverse()
            result += Command._table_cell_separator.join(row)
            result += "\\n"
        self.CONTENT_BUFFER.clear()
        return self._prefix + result + self._suffix
