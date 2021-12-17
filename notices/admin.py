from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(models.Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "desc",
        "tag",
    )