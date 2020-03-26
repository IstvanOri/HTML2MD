import os

from converter.Rule import Rule


# TODO: duplicate code, see Transformer.py
def _get_class(kls):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m


class Rules():
    """
    The complete ruleset generated from the rulebook.txt file.
    """
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def __init__(self):
        self._rules = {}
        rulebook_file = open(self.__location__+os.sep+"rulebook.txt", "r")
        for x in rulebook_file:
            if not x.startswith("//"):
                entry = x.split(":")
                selector = entry[0]
                setup = entry[1].split(">")
                rule = Rule(selector)
                for command in setup:
                    command_name = command[:command.find("(")]
                    command_args = command[command.find("(")+1:command.rfind(")")]
                    command_args_list = list(command_args.split(","))
                    command_args_dict = {i: command_args_list[i] for i in range(0, len(command_args_list))}
                    command_class_name = _get_class("commands."+command_name+"."+command_name)
                    command_class_type = type(command_name, (command_class_name,), command_args_dict)
                    rule.add_command(command_class_type(command_args_dict))
                self._rules.update({selector: rule})
        rulebook_file.close()

    @property
    def rules(self) -> [Rule]:
        return self._rules
