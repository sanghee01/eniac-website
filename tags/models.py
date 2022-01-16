from django.contrib.admin.decorators import register
from django.db import models

from core.models import TimeStampedModel
# Create your models here.

class Tag(TimeStampedModel):
    name = models.CharField(max_length=32, verbose_name="태그명")

    def __str__(self):
        return self.name 