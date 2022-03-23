from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Activity)
class ActivitiyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "desc",
        "semester",
    )


@admin.register(models.Act_Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


# Register your models here.
@admin.register(models.Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = (
        "desc",
    )
