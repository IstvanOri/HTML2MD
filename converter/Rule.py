from commands.Command import Command


class Rule():
    """
    A Rule is a command assigned to a tag. The configuration is in the rulebook.txt
    """

    def __init__(self, selector: str):
        self._selector: str = selector
        self._commands: [Command] = []

    @property
    def selector(self):
        return self._selector

    @property
    def commands(self):
        return self._commands

    def add_command(self, command: Command):
        self._commands.append(command)
