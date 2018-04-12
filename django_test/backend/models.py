from django.db import models

from django_test.db.fields import *

# Create your models here.


class BaseItem(models.Model):
    name = models.CharField(max_length=20,default='')

    def __str__(self):
        return '%s-%s' %(self.id ,self.name)



class BaseTable(models.Model):
    name = models.CharField(max_length=20,default='')
    items = models.ManyToManyField(BaseItem)

    created_at = AutoUnixTimestampField(editable=False)
    updated_at = AutoUnixTimestampField(auto_created=True, editable=False)



