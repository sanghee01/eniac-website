from django import forms
from . import models

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                print(user.check_password(password))
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))



class SignUpForm(forms.ModelForm):
    
  
   
    username = forms.CharField(help_text=False)
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    class Meta:
        model = models.User
        fields = ("email", "git_url", "fav_pro_genre", "major")

    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exists with that email")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password 

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        git_url = self.cleaned_data.get("git_url")
        fav_pro_genre = self.cleaned_data.get("fav_pro_genre")
        major = self.cleaned_data.get("major")
        user.username = username
        user.email = email
        user.git_url = git_url
        user.fav_pro_genre = fav_pro_genre
        user.major = major
        user.set_password(password)
        user.save()

    # 계정을 생성하는 함수
  


        # 바셀했고