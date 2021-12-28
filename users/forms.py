from django import forms
from . import models

class SignUpForm(forms.Form):

    pass

    # name = forms.CharField(max_length=80)
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    # password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    # name = forms.CharField(max_length=80)
    # major = forms.CharField(max_length=80)
    # git_url = forms.CharField(max_length=80)
    # eniac_code = forms.IntegerField(null=True)
    # fav = forms.CharField(max_length=30)
    # resolution = forms.CharField(max_length=200)


    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     try:
    #         models.User.objects.get(email=email)
    #         raise forms.ValidationError("User already exists with that email")
    #     except models.User.DoesNotExist:
    #         return email

    # def clean_password1(self):
    #     password = self.cleaned_data.get("password")
    #     password1 = self.cleaned_data.get("password1")
    #     if password != password1:
    #         raise forms.ValidationError("Password confirmation does not match")
    #     else:
    #         return password 