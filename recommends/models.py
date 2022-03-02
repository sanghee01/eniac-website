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

    LEC_BOOK = "강의"
    LEC_BOOK = "책"

    LEC_BOOK_CHOICES = (
      (LEC_BOOK, "강의"),
      (LEC_BOOK, "책"),
    )

    LEVEL_A = "입문"
    LEVEL_B = "주니어"

    LEVEL_CHOICES = (
      (LEVEL_A, "입문"),
      (LEVEL_B, "주니어"),
    )


    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    img = models.ImageField(null=True)

    genre = models.CharField(choices=GENRE_CHOICES, max_length=20, blank=True, null=True)

    lec_book = models.CharField(choices=LEC_BOOK_CHOICES, max_length=20, blank=True, null=True)


    level = models.CharField(choices=LEVEL_CHOICES, max_length=20, blank=True, null=True)


    # 여기서 강의냐 책이냐 이거를 또 구분해야한다


    class Meta:
        ordering = ["-created"]

 
    @property
    def get_photo_url(self):
      if self.img:
          return self.img.url
      else:
          return "/static/images/coding.jpg"


    