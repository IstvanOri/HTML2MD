from abc import ABC
from html.parser import HTMLParser

from commands.Command import Command
from converter.Rules import Rules


class HTML2MDParser(HTMLParser, ABC):
    """
    An HTMLParser instance that converts the HTML feed to MD by the Rules specified in the rulebook.
    """
    _rules: Rules = Rules()

    def __init__(self):
        super().__init__()
        self._roots = []
        self._result = ""
        self._commands = []

    def handle_starttag(self, tag, attrs):
        if tag in self._rules.rules:
            first = True
            for command in self._rules.rules.get(tag).commands:
                cmd: Command = command.__copy__()
                cmd.attrs = attrs
                cmd.tag = tag
                if len(self._commands) > 0:
                    self._commands[-1].add_child(cmd)
                    self._commands[-1].data += "[:child:]"
                    cmd.ancestor = self._commands[-1]
                self._commands.append(cmd)
                if first:
                    first = False
                else:
                    cmd.pop_more()

    def handle_endtag(self, tag):
        if tag in self._rules.rules and len(self._commands) > 0:
            while self._commands.pop().needs_more_pop():
                pass

    def handle_data(self, data):
        if len(self._commands) == 1:
            self._roots.append(self._commands[0])
        if len(self._commands) > 0:
            self._commands[-1].data += data

    def result(self):
        return self._roots[0].execute()
