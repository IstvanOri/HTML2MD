import errno
import io
import os
import sys
from builtins import print

from html2md.converter.HTML2MDParser import HTML2MDParser
from html2md.transformers.Transformer import Transformer


def run(argv):
    _name_log_file = None
    if len(argv) < 2:
        sys.exit("Two arguments are expected. First is the input file or directory, the second is the output directory.")
    if not os.path.isdir(argv[2]):
        sys.exit("Second argument has to be an existing directory for the output.")
    if "--names" in argv:
        _name_log_file = open(argv[2] + os.sep + 'name_changes_log.csv', 'w')
    if os.path.isfile(argv[1]):
        convert(argv[1], argv[2])
    if os.path.isdir(argv[1]):
        for root, subdirs, files in os.walk(argv[1]):
            for file in files:
                if file.endswith(".html"):
                    result = convert(root+os.sep+file)
                    relative_path = os.path.relpath(root, argv[1])
                    transformer = Transformer()
                    file_to_write = transformer.filename_transform(file)
                    write(result, argv[2] + os.sep + relative_path + os.sep+file_to_write)
                    if _name_log_file is not None:
                        _name_log_file.write(relative_path + os.sep + file + ';' + relative_path + os.sep + file_to_write + '\n')
    if _name_log_file is not None:
        _name_log_file.flush()
        _name_log_file.close()
        _name_log_file = None


def convert(file_name: str) -> str:
    print("processing "+file_name+"...")

    with io.open(file_name, 'r', encoding='utf8') as file:
        parser = HTML2MDParser()
        transformer = Transformer()
        text = transformer.pre_transform(file.read())
        file.close()
        parser.reset()
        parser.feed(text)
        return transformer.post_transform(parser.result())


def write(content: str, file_name: str):
    if not os.path.exists(os.path.dirname(file_name)):
        try:
            os.makedirs(os.path.dirname(file_name))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    print("writing "+file_name)
    f = open(file_name, "wb")
    f.write(content.encode('utf-8'))
    f.flush()
    f.close()
