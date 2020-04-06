from html2md.commands.Command import Command
from html2md.commands.Table import Table


class RowFeed(Command):
    def __init__(self, args):
        super().__init__()

    def __copy__(self):
        return RowFeed(None)

    def execute(self) -> str:
        for child in self._children:
            child.execute()
        Table.CONTENT_BUFFER.row_feed()
        return ""