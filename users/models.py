from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.shortcuts import reverse
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from config import settings



# Create your models here.
class User(AbstractUser): 
    GENRE_WEB = "WEB"
    GENRE_APP = "APP"
    GENRE_AI = "AI"
    GENRE_GAME = "GAME"
    GENRE_OTHER = "OTHER"

    GENRE_CHOICES = (
      (GENRE_WEB, "WEB"),
      (GENRE_APP, "APP"),
      (GENRE_AI, "AI"),
      (GENRE_GAME, "GAME"),
      (GENRE_OTHER, "OTHER")
    )
    username = models.CharField(max_length=20, blank=True, null=True)
    major = models.CharField(max_length=20, blank=True, null=True)
    git_url = models.URLField(max_length=200, null=True, blank=True)
    eniac_code = models.CharField(max_length=20, null=True, blank=True)
    entered_eniac = models.SmallIntegerField(default=32, max_length=10)
    fav_pro_genre = models.CharField(max_length=20, blank=True, null=True)
    blog_url = models.URLField(default=32, max_length=200)

    student_id = models.IntegerField( max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=40, blank=True, null=True)
    
    email_confirmed = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)

    

    def get_absolute_url(self):
        return reverse("user:profile", kwargs={'pk': self.pk})

    def verify_email(self):
        if self.email_confirmed is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "에니악 인증호가인",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                html_message=html_message,
            )

            self.save()
        return

