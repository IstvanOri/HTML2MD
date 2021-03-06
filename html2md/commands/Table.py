from html2md.commands.Command import Command
import re

from html2md.commands.TableBuffer import TableBuffer


class Table(Command):
    """
        Constructs a table. The header will be the first row of the children
    """
    def __init__(self, args):
        super().__init__()
        self._content_buffer = TableBuffer()
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
        cell_separator = Command._table_cell_separator
        result += cell_separator + cell_separator.join(self._content_buffer.rows[0]) + cell_separator
        result += "\\n"
        row_sep = [Command._table_head_separator] * len(self._content_buffer.rows[0])
        result += cell_separator + cell_separator.join(row_sep) + cell_separator
        result += "\\n"
        for row in self._content_buffer.rows[1:]:
            for i in range(len(row), len(self._content_buffer.rows[0])):
                row.reverse()
                row.append("")
                row.reverse()
            result += cell_separator + cell_separator.join(row) + cell_separator
            result += "\\n"
        self._content_buffer.clear()
        return self._prefix + result + self._suffix
