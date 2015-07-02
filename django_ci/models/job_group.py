from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django_ci.models import ActivableModel, DataIngestionManager


@python_2_unicode_compatible
class JobGroup(ActivableModel):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=10L, default='?')
    name = models.CharField(max_length=50L)
    description = models.TextField(blank=True, default='fill me')

    objects = DataIngestionManager()

    def __str__(self):
        return "{0} ({1})".format(
            self.name, self.symbol)