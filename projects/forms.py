from django import forms
from . import models


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = (
            "title",
            "desc",
            "thumnail_img",
            "tag",
            "git",
 
        )

    def save(self, *args, **kwargs):
        project = super().save(commit=False)
        return project