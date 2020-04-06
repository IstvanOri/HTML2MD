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
        Table.CONTENT_BUFFER.cell_feed(cell_content)
        for attr in self._attrs:
            if attr[0] == "colspan":
                for i in range(1, int(attr[1])):
                    Table.CONTENT_BUFFER.cell_feed("")
        return ""