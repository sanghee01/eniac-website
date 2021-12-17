from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import TimeStampedModel
# Create your models here.
class Challenge(TimeStampedModel): 
    desc = models.TextField(max_length=300)
    users = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="challenge_user",  null=False, blank=False
    ) 

class Challenge_Comment(TimeStampedModel):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='chall_comments', null=True)
    desc = models.TextField(max_length=300)
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="chall_users",   null=False, blank=False
    )

    def __str__(self):
        return self.desc

    class Meta:
        db_table = 'chall_comments'

