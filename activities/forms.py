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

        widgets = {
            "desc": forms.TextInput(attrs={'placeholder': '댓글을 입력헤주세요'}),  
        }

    
    

class CreateActivityForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = (
          "title",
          "desc",
          "semester",
          "thumnail_img",
        )
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': '프로젝트 이름'}),  
            # "semester": forms.TextInput(attrs={'placeholder': '학기를 적적어어주주세세요'}),        
            "desc": forms.TextInput(attrs={'placeholder': '간단한 설명을 적어주세요'}),
            "thumnail_img": forms.FileInput(attrs={'placeholder': '사용할 이미지를 넣어주세요'}),
            # "tag": forms.TextInput(attrs={'placeholder': '태그를 ,로 구분해주세요'})         
        }

        labels = {
            "title": "제목",
            "semester": "학기",
            "thumnail_img": "이미지첨부",
            "tag": "태그",

        }

    def save(self, *args, **kwargs):
        project = super().save(commit=False)
        return project