from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(models.Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = (
        "users",
        "desc",
    )

@admin.register(models.Challenge_Comment)
class CommentAdmin(admin.ModelAdmin):
    pass