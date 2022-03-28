from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import TimeStampedModel
from django.urls import reverse

# Create your models here.
class Project(TimeStampedModel): 
    title = models.CharField(max_length=100, null=True,  default = '', verbose_name='제목')
    desc = models.TextField(max_length=300, default = '', null=True, verbose_name='내용')
    image = models.ImageField(blank=True)
    thumnail_img = models.ImageField(upload_to="", verbose_name='썸네일 이미지')
    tag = models.CharField(max_length=40, verbose_name='태그')
    git = models.CharField(max_length=60, verbose_name='깃허브 주소')
    views = models.PositiveIntegerField(default=0, verbose_name='조회수')
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="project",  null=True, blank=False
    ) 

    developer = models.CharField(max_length=200, verbose_name='개발자')

    class Meta:
        ordering = ["-created"]
        
    @property
    def get_photo_url(self):
      if self.thumnail_img:
          return self.thumnail_img.url
      else:
          return "/static/images/user.jpg"

    def get_absolute_url(self):
        return reverse("project:detail", kwargs={"pk": self.pk})


