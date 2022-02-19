from django import forms
from . import models


class CreateChallengeForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = (
            "desc",
        )
        widgets = {
           "desc": forms.TextInput(attrs={'placeholder': '내용을 작성해주세요'}),          
        }

    def save(self, *args, **kwargs):
        project = super().save(commit=False)
        return project

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = models.Act_Comment
        fields = (
            "desc",
        )