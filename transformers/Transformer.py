import os


# TODO: duplicate code, see Rules.py
from transformers.Tranformation import Transformation


def _get_class(kls):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m


class Transformer:

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def __init__(self):
        self._pre_transformations: [Transformation] = self._read_config("pretransform")
        self._post_transformations: [Transformation] = self._read_config("posttransform")

    def pre_transform(self, target):
        result = target
        for tr in self._pre_transformations:
            result = tr.execute(result)
        return result

    def post_transform(self, target):
        result = target
        for tr in self._post_transformations:
            result = tr.execute(result)
        return result

    def _read_config(self, file_name: str) -> [Transformation]:
        transformations: [Transformation] = []
        transformations_file = open(self.__location__ + os.sep + file_name + ".txt", "r")
        for x in transformations_file:
            if not x.startswith("#"):
                transformation_name = x[:x.find("(")]
                transformation_args = x[x.find("(")+1:x.rfind(")")]
                transformation_args_list = transformation_args.split(",")
                transformation_args_dict = {i: transformation_args_list[i] for i in range(0, len(transformation_args_list))}
                transformation_class_name = _get_class("transformers."+transformation_name+"."+transformation_name)
                transformation_class_type = type(transformation_name, (transformation_class_name,), transformation_args_dict)
                transformations.append(transformation_class_type(transformation_args_dict))
        transformations_file.close()
        return transformations
