import re

from html2md.commands.Command import Command


class VariableResolver:

    def resolve(self, text: str) -> str:
        resolved = text
        varPattern = re.compile(r'\$\{(.*)\}')
        variables = re.findall(varPattern, text)
        for var in variables:
            try:
                if getattr(Command, var) is not None:
                    resolved = resolved.replace("${"+var+"}", str(getattr(Command, var)))
            except AttributeError:
                pass
        return resolved
