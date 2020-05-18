import re

from html2md.commands.Command import Command


class VariableResolver:
    """
    Resolves config values referenced in ${variable} form.

    Currently supported variables:
        _bullet (default: ' * ')
        _table_cell_separator (default: ' | ')
        _table_head_separator (default: '---')
        _level (default: 0)
    """

    def resolve(self, text: str) -> str:
        """
        Resolves variables in a string.
        :return: The resolved string in which all known ${var} references are replaced by the variable's value
        """
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
