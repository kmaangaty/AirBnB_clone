#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel"""

    def __init__(self, *args, **kwargs):
        """BaseModel"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """BaseModel"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """save"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """to_dict"""
        dc = {}
        dc.update(self.__dict__)
        dc.update(
            {'__class__': (str(type(self))
            .split('.')[-1]).split('\'')[0]}
        )
        dc['created_at'] = self.created_at.isoformat()
        dc['updated_at'] = self.updated_at.isoformat()
        return dc
