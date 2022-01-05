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





class SignUpForm(forms.Form):

    class Meta:
        model = models.User
        fields = ("name", "email", "major", "git_url", "eniac_code", "fav", "resolution")


  
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
   
    
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

    def save(self):
        name = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        major = self.cleaned_data.get("major")
        git_url = self.cleaned_data.get("git_url")
        eniac_code = self.cleaned_data.get("eniac_code")
        fav = self.cleaned_data.get("fav")

        user = models.User.objects.create_user(email, email, password)
        # 왜 이메일을 두번하는거지..?
        user.username = email
        user.set_password(password)
        user.save()

        # 이제 기서 save쪽을