#!/usr/bin/python3
import uuid
import datetime
import models
import json

"""

base_model module defines a class BaseModel with attributes
id, created_at, updated_at and public instance methods
save and to_dict
"""


class BaseModel:
    """BaseModel class defines all common attributes and methods
    that will inherit from it
    """

    def __init__(self, *args, **kwargs):
        if bool(kwargs):
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k in ['created_at', 'updated_at']:
                    v = datetime.datetime.fromisoformat(v)
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}" \
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dict = {}
        for key, value in self.__dict__.items():
            if type(value) is datetime.datetime:
                value = value.isoformat()
            my_dict[key] = value
        my_dict['__class__'] = type(self).__name__
        return my_dict

    @staticmethod
    def get_single_record(inst_id):
        record_found = None
        all_records = models.storage.all()
        for record in all_records.values():
            if record.id == inst_id:
                record_found = record
            else:
                continue
        if record_found is None:
            print("** no instance found **")
            return
        else:
            return record_found

    @staticmethod
    def delete_record(inst_id):
        with open("file.json", "r") as file:
            data = json.load(file)
            if inst_id not in [j['id'] for i, j in data.items()]:
                print("** no instance found **")
                return
            else:
                data = {i: j for i, j in data.items() if j['id'] != inst_id}
        with open("file.json", "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def get_all_records():
        return models.storage.all()

    @staticmethod
    def update_record(**kwargs):
        record = kwargs.get('record')
        attr_name = kwargs.get('attr_name')
        attr_value = kwargs.get('attr_value')
        setattr(record, attr_name, attr_value.replace('"', ''))
        models.storage.save()
