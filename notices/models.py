from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import TimeStampedModel
from taggit.managers import TaggableManager
from taggit.models import (
    TagBase, TaggedItemBase
)



# Create your models here.
class Notice(TimeStampedModel): 
    title = models.CharField(max_length=100)
    thumnail_img = models.ImageField()
    desc = models.TextField(max_length=300)
    tag = models.ManyToManyField('tags.Tag', verbose_name='태그')
    
    class Meta:
        ordering = ["-created"]


    @property
    def get_photo_url(self):
      if self.thumnail_img:
          return self.thumnail_img.url
      else:
          return "/static/images/coding.jpg"


