import importlib
import inspect
import os

from models.base_model import BaseModel


def get_classes():
    base_folder = "models"
    classes = []
    for subdir, dirs, files in os.walk(base_folder):
        for file in files:
            if file.endswith('.py'):
                module_name = subdir.replace(os.path.sep,
                                             '.') + '.' + file[:-3]
                try:
                    module = importlib.import_module(module_name)
                    classes.extend([member[1] for member in
                                    inspect.getmembers(module,
                                                       inspect.isclass)])
                except ImportError:
                    pass
    return [{i.__name__: i} for i in set(classes) if
            issubclass(i, BaseModel) or i.__name__ == "BaseModel"]


def get_formatted_records(model_classes, model_name):
    model_instance = [i.get(model_name) for i in model_classes][0]()
    results = [i.__str__() for i in model_instance.get_all_records().values()]
    return results
