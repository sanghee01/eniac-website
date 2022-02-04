from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import TimeStampedModel

# Create your models here.
class Recommend(TimeStampedModel): 

    GENRE_WEB = "웹"
    GENRE_APP = "앱"
    GENRE_AI = "AI"
    GENRE_GAME = "게임"
    GENRE_SECURE = "보안"
    GENRE_OTHER = "OTHER"

    GENRE_CHOICES = (
      (GENRE_WEB, "웹"),
      (GENRE_APP, "앱"),
      (GENRE_AI, "AI"),
      (GENRE_GAME, "GAME"),
      (GENRE_SECURE, "보안"),
      (GENRE_OTHER, "OTHER")
    )



    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    img = models.ImageField(null=True)

    genre = models.CharField(choices=GENRE_CHOICES, max_length=20, blank=True, null=True)

    class Meta:
        ordering = ["-created"]

 
    @property
    def get_photo_url(self):
      if self.img:
          return self.img.url
      else:
          return "/static/images/coding.jpg"


    