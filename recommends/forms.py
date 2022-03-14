from django import forms
from . import models


class CreateNoticeForm(forms.ModelForm):
    class Meta:
        model = models.Recommend
        fields = (
            "title",
            "desc",
            "img",
            "genre",
            "level",
            "lead",
 
        )
        widgets = {
           
            
          
        
        }

        labels = {
           
        }

    def save(self, *args, **kwargs):
        project = super().save(commit=False)
        return project