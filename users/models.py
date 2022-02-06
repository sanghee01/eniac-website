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

    major = models.CharField(max_length=20, blank=False, null=False)
    git_url = models.URLField(max_length=200)
    eniac_code = models.CharField(max_length=20, null=False, blank=False)
    entered_eniac = models.CharField(default=32, max_length=10)
    fav_pro_genre = models.CharField(choices=GENRE_CHOICES, max_length=20, blank=True, null=True)

  

    

    def get_absolute_url(self):
        return reverse("user:profile", kwargs={'pk': self.pk})

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "email/verify_email.html", {"secret": secret}
            )
            send_mail(
                "Verify Hairbnb Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                html_message=html_message,
            )

            self.save()
        return
