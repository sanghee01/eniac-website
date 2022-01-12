from django.contrib import admin
from . import models
from .models import Tag


# Register your models here.
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

