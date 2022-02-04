from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import TimeStampedModel

# Create your models here.
class Recommend(TimeStampedModel): 
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    img = models.ImageField(null=True)

    class Meta:
        ordering = ["-created"]

 
    @property
    def get_photo_url(self):
      if self.thumnail_img:
          return self.thumnail_img.url
      else:
          return "/static/images/coding.jpg"


    