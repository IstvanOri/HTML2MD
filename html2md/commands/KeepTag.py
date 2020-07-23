import re

from html2md.commands.Command import Command


class KeepTag(Command):
    """
    Command that keeps the original HTML tag. Any number of parameters can be passed for this Command. If no
    parameters are passed, all attributes will be kept. If at least one parameter is passed, then only those
    attributes will be kept that are in the parameter list.
    """

    SHORT_TAGS = ["img", "br"]

    def __init__(self, args):
        super().__init__()
        self._whitelist = []
        for key, value in args.items():
            self._whitelist.append(value)

    def __copy__(self):
        return KeepTag({i: self._whitelist[i] for i in range(0, len(self._whitelist))})

    def execute(self) -> str:
        """
        Returns the content linearized
        :return: "The content without linebrakes"
        """
        result = "<" + self.tag
        for attr in self._attrs:
            if len(self._whitelist) == 0 or attr[0] in self._whitelist:
                result += " "+attr[0] + "=\"" + attr[1] + "\""
        if self.tag in self.SHORT_TAGS:
            result += "/>"
        else:
            result += ">"
            result += super().execute()
            result += "</" + self.tag + ">"
        return result
