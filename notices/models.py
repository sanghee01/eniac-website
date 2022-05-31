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
    title = models.CharField(max_length=100, verbose_name='제목')
    thumnail_img = models.ImageField(verbose_name='썸네일')
    img_a = models.ImageField(verbose_name='이미지1', null=True, blank=True)
    img_b = models.ImageField(verbose_name='이미지2', null=True, blank=True)
    img_c = models.ImageField(verbose_name='이미지3', null=True, blank=True)
    desc = models.TextField(max_length=300, verbose_name='내용')
    tag = models.ManyToManyField('tags.Tag', verbose_name='학년별')
    # activity_tag = models.ManyToManyField('tags.ActivityTag', verbose_name='활동별')
    # seme_tag = models.ManyToManyField('tags.SemeTag', verbose_name='학기별')
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="notices",  null=True, blank=False
    ) 
    class Meta:
        ordering = ["-created"]

 
    @property
    def get_photo_url(self):
      if self.thumnail_img:
          return self.thumnail_img.url
      else:
          return "/static/images/coding.jpg"

    @property
    def get_photo_url_a(self):
      if self.img_a:
          return self.img_a.url
      else:
          return None

    @property
    def get_photo_url_b(self):
      if self.img_b:
          return self.img_b.url
      else:
          return None

    @property
    def get_photo_url_c(self):
      if self.img_c:
          return self.img_c.url
      else:
          return None 


    