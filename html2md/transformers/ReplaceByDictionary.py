import os
import re
from builtins import print

from html2md import LOCATIONS
from html2md.transformers.Tranformation import Transformation


class ReplaceByDictionary(Transformation):
    """
    Transformation that replaces all occurrences based on a dictionary file. The file has to be in the config
    directory. The first and only parameter should be the relative path of the dictionary file in the config
    directory. The dictionary file should contain lines that are the matcher and the replacement separeted by commas.
    """

    def __init__(self, args):
        self._dictionary_ = args[0]

    def execute(self, content: str) -> str:
        result = ""

        rules = []
        transformations_file = open(LOCATIONS["CONFIG_DEFAULT"] + os.sep + self._dictionary_, "r")
        for entry in transformations_file:
            rules.append(entry.strip().split(','))
        transformations_file.close()
        for line in content.splitlines(True):
            transformed_line = line
            for rule in rules:
                transformed_line = re.sub(re.compile(rule[0]), rule[1], transformed_line)
            result += transformed_line
        return result
