import importlib
import inspect
import os

from models import storage
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


def classes_to_str_list(model_classes):
    return [list(d.keys())[0] for d in model_classes]


def get_formatted_records(model_classes, model_name):
    records = storage.all()
    results = [i.__str__() for i in records.values() if i.__class__.__name__ == model_name]
    return results
