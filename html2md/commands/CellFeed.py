from html2md.commands.Command import Command
from html2md.commands.Table import Table


class CellFeed(Command):
    def __init__(self, args):
        super().__init__()
        self._rowspan = []

    def __copy__(self):
        return CellFeed(None)

    def execute(self) -> str:
        cell_content = super().execute()
        table = self.ancestor
        while table.tag != "table":
            table = table.ancestor
        cell_content = cell_content.replace("\\n", " ")
        table._content_buffer.cell_feed(cell_content)
        for attr in self._attrs:
            if attr[0] == "colspan":
                for i in range(1, int(attr[1])):
                    table._content_buffer.cell_feed("")
        return ""