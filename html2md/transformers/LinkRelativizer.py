import re

from html2md.transformers.Tranformation import Transformation


class LinkRelativizer(Transformation):
    """
    Transformation that accepts any number of URLs as argument and makes all absolute links starting with one of
    those URLs to relative
    """

    def __init__(self, args):
        self._urls = []
        for i in args:
            self._urls.append(args[i])
        pass

    def execute(self, content: str) -> str:
        result = content
        for url in self._urls:
            links = re.compile(r'(\(){}([^\)]*)'.format(url))
            result = re.sub(links, r'\g<1>\g<2>', result)
        return result
