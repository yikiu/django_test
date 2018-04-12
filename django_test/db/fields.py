from django.db import models
from datetime import datetime
from time import strftime


#
# Custom field types in here.
#
class UnixTimestampField(models.DateTimeField):
    """
    """

    def __init__(self, null=False, blank=False, auto_updated=None, default=None, **kwargs):
        super(UnixTimestampField, self).__init__(**kwargs)
        self.default = default
        self.auto_updated = auto_updated
        # default for TIMESTAMP is NOT NULL unlike most fields, so we have to
        # cheat a little:
        self.blank, self.isnull = blank, null
        self.null = True  # To prevent the framework from shoving in "not null".

    def db_type(self, connection):
        typ = ['TIMESTAMP ']
        # See above!
        if self.isnull:
            typ += ['NULL']
        if self.auto_created:
            typ += ['default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP']
        return ' '.join(typ)

    def to_python(self, value):
        return datetime.fromtimestamp(value)

    def get_db_prep_value(self, value, connection, prepared=False):
        if isinstance(value, datetime):
            return value.timestamp()
        return value

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        return name, path, args, kwargs


class AutoUnixTimestampField(UnixTimestampField):
    """
    """

    def db_type(self, connection):
        typ = ['TIMESTAMP default CURRENT_TIMESTAMP']
        if self.auto_created:
            typ += ['default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP']
        return ' '.join(typ)

    def get_db_prep_value(self, value, connection, prepared=False):
        pass

