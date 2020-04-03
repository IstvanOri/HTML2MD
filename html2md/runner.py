import os
import sys

from html2md.converter.HTML2MDParser import HTML2MDParser
from html2md.transformers.Transformer import Transformer


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
                if file.endswith(".html"):
                    result = convert(root+os.sep+file)
                    write(result, argv[2], os.path.basename(root+os.sep+file).replace(".html",".md"))


def convert(file_name: str) -> str:
    print("processing "+file_name+"...")
    file = open(file_name, 'r')
    parser = HTML2MDParser()
    transformer = Transformer()
    text = transformer.pre_transform(file.read())
    file.close()
    parser.reset()
    parser.feed(text)
    return transformer.post_transform(parser.result())


def write(content: str, output_dir: str, file_name: str):
    f = open(output_dir + os.sep + os.path.basename(file_name), "wb")
    f.write(content.encode('utf-8'))
    f.flush()
    f.close()
