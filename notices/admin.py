from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(models.Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "desc",
        'tag_list', 
    )
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    
    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())