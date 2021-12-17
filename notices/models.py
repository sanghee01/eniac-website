from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import TimeStampedModel

# Create your models here.
class Notice(TimeStampedModel): 
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=40)
    thumnail_img = models.ImageField()
    desc = models.TextField(max_length=300)


