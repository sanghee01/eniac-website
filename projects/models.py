from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import TimeStampedModel

# Create your models here.
class Project(TimeStampedModel): 
    title = models.CharField(max_length=100, null=True,  default = '')
    desc = models.TextField(max_length=300, default = '', null=True,)
    image = models.ImageField(blank=True)
    thumnail_img = models.ImageField(upload_to="")
    tag = models.CharField(max_length=40)
    git = models.CharField(max_length=60)
    views = models.PositiveIntegerField(default=0, verbose_name='조회수')
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="project",  null=False, blank=False
    ) 
    class Meta:
        ordering = ["-created"]
        
    @property
    def get_photo_url(self):
      if self.thumnail_img:
          return self.thumnail_img.url
      else:
          return "/static/images/user.jpg"


