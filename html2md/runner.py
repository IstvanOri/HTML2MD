import os
import sys

from html2md.converter.HTML2MDParser import HTML2MDParser
from html2md.transformers.Transformer import Transformer


# TODO: Transform this to PIP package and remove main.py
def run(argv):
    if len(argv) < 2:
        sys.exit("Two arguments are expected. First is the input file or directory, the second is the output directory.")
    if not os.path.isdir(argv[2]):
        sys.exit("Second argument has to be an existing directory for the output.")
    if os.path.isfile(argv[1]):
        convert(argv[1], argv[2])
    if os.path.isdir(argv[1]):
        for root, subdirs, files in os.walk(argv[1]):
            for file in files:
                convert(root+os.sep+file, argv[2])


def convert(file_name: str, output_dir: str):
    if file_name.endswith(".html"):
        print("processing "+file_name+" ...")
        file = open(file_name, 'r')
        parser = HTML2MDParser()
        transformer = Transformer()
        text = transformer.pre_transform(file.read())
        parser.reset()
        parser.feed(text)
        result = transformer.post_transform(parser.result())
        f = open(output_dir + os.sep + os.path.basename(file_name).replace(".html","") + ".md", "wb")
        f.write(result.encode('utf-8'))
        f.flush()
        f.close()
