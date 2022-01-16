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
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': '프로젝트 이름'}),          
            "desc": forms.TextInput(attrs={'placeholder': '간단한 설명을 적어주세요'}),
            "thumnail_img": forms.FileInput(attrs={'placeholder': '사용할 이미지를 넣어주세요'}),
            "tag": forms.TextInput(attrs={'placeholder': '태그를 ,로 구분해주세요'}),
            "git": forms.TextInput(attrs={'placeholder': '깃허브 링크를 적어주세요'}),
          
           

        }

    def save(self, *args, **kwargs):
        project = super().save(commit=False)
        return project