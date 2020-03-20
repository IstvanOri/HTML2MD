from pprint import pprint

from commands.Command import Command


class WrapWithAttribute(Command):

    def __init__(self, args):
        super().__init__()
        self._prefix: str = args[0]
        self._suffix: str = args[1]
        self._attr_name: str = args[2]
        self._attr_prefix: str = args[3]
        self._attr_suffix: str = args[4]

    def __copy__(self):
        return WrapWithAttribute((self._prefix, self._suffix, self._attr_name, self._attr_prefix, self._attr_suffix))

    def execute(self) -> str:
        attr_part = self._attr_prefix
        for attr in self._attrs:
            if attr[0] == self._attr_name:
                attr_part += attr[1]
        attr_part += self._attr_suffix
        return self._prefix + self.data + self._suffix + attr_part
