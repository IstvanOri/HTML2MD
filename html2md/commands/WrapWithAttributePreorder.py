from html2md.commands.Command import Command


class WrapWithAttributePreorder(Command):

    def __init__(self, args):
        super().__init__()
        self._prefix: str = args[0]
        self._suffix: str = args[1]
        self._attr_name: str = args[2]
        self._attr_prefix: str = args[3]
        self._attr_suffix: str = args[4]
        self._allow_empty: str = args[5]

    def __copy__(self):
        return WrapWithAttributePreorder((self._prefix, self._suffix, self._attr_name, self._attr_prefix, self._attr_suffix, self._allow_empty))

    def execute(self) -> str:
        attr_part = self._attr_prefix
        for attr in self._attrs:
            if attr[0] == self._attr_name:
                attr_part += attr[1]
        attr_part += self._attr_suffix
        content = super().execute()
        if len(content) == 0 and not self._allow_empty:
            return ""
        return attr_part + self._prefix + content + self._suffix
