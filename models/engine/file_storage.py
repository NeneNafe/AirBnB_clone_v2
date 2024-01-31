#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    __classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
                }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls and cls in list(self.__cls.value()):
            sub = {}
            sub.update(FileStorage.__objects)
            return {key: val for key, val in sub.items()
                    if key[0:k.find(".")] == cls.__name__}
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """deletes obj from __objects"""
        temp = {}
        temp.update(FileStorage.__objects)
        if obj:
            new = {key: val for key, val in temp.items() if val != obj}
            FileStorage.__objects = new
            self.save()

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.lod(f)
                for key, val in temp.items():
                    self.all()[key] = self.__cls[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """deserializes the JSON file to objects"""
        self.reload()
