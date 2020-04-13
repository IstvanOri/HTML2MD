from abc import ABC
from html.parser import HTMLParser

from html2md.commands.Command import Command
from html2md.converter.Rules import Rules


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
        self._is_root_command = True
        self._last_encountered_tag = None
        self._last_encountered_attributes = None

    def handle_starttag(self, tag, attrs):
        self._is_root_command = True
        self._last_encountered_tag = tag
        self._last_encountered_attributes = attrs
        if tag in self._rules.rules:
            for command in self._rules.rules.get(tag).commands:
                self.execute_command(command)
                self._is_root_command = False
        for attr in attrs:
            self.attribute_selector_handler(attr, "class", ".")
            self.attribute_selector_handler(attr, "id", "#")

    def attribute_selector_handler(self, attr, name, prefix):
        if attr[0] == name:
            for cl in attr[1].split():
                if self._rules.rules.get(prefix + cl) is not None:
                    for command in self._rules.rules.get(prefix + cl).commands:
                        self.execute_command(command)
                        self._is_root_command = False

    def execute_command(self, command):
        cmd: Command = command.__copy__()
        cmd.attrs = self._last_encountered_attributes
        cmd.tag = self._last_encountered_tag
        if len(self._commands) > 0:
            self._commands[-1].add_child(cmd)
            self._commands[-1].data += "[:child:]"
            cmd.ancestor = self._commands[-1]
        self._commands.append(cmd)
        if not self._is_root_command:
            cmd.pop_more()

    def handle_endtag(self, tag):
        if tag == "br":
            print("br")
            self.handle_starttag("br", [])
        if tag in self._rules.rules and len(self._commands) > 0:
            while self._commands.pop().needs_more_pop():
                pass

    def handle_data(self, data):
        if len(self._commands) >= 1 and len(self._roots) == 0:
            self._roots.append(self._commands[0])
        if len(self._commands) > 0:
            self._commands[-1].data += data

    def result(self):
        if len(self._roots) > 0:
            return self._roots[0].execute()
        return ""
