class TableBuffer:

    def __init__(self):
        self._cells = []
        self._rows = []


    @property
    def rows(self):
        return self._rows

    def cell_feed(self, content):
        self._cells.append(content)

    def row_feed(self):
        self._rows.append(self._cells)
        self._cells = []

    def clear(self):
        self._cells = []
        self._rows = []