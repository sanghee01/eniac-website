from django import forms
from . import models


class CreateNoticeForm(forms.ModelForm):
    class Meta:
        model = models.Notice
        fields = (
            "title",
            "desc",
            "thumnail_img",  
            "img_a",   
            "img_b", 
            "img_c", 
            "tag",
 
        )
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': '공지제목'}),          
          
            "thumnail_img": forms.FileInput(attrs={'placeholder': '사용할 이미지를 넣어주세요'}),
            "img_a": forms.FileInput(attrs={'placeholder': '사용할 이미지를 넣어주세요'}),
            "img_b": forms.FileInput(attrs={'placeholder': '사용할 이미지를 넣어주세요'}),
            "img_c": forms.FileInput(attrs={'placeholder': '사용할 이미지를 넣어주세요'}),
            # "tag": forms.TextInput(attrs={'placeholder': '태그를 ,로 구분해주세요'}),
            
          
        
        }

        labels = {
            "title": "제목",
            "thumnail_img": "썸네일",
            "tag": "태그",
            "desc": "내용",

        }

    def save(self, *args, **kwargs):
        project = super().save(commit=False)
        return project