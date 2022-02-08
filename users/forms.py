from secrets import choice
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

    # 이메일 비번 성명 전번 학과 기수
    # 관심분야 깃주소 블로그주소
    
    username = forms.CharField(help_text=False, widget=forms.TextInput(attrs={'placeholder': '이름을 입력해주세요'}), label='이름')
    major = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '전공을 입력해주세요'}), label='전공')
    entered_eniac = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '기수를 입력해주세요'}), label='에니악기수')
    fav_pro_genre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '선호분야를 입력해주세요'}), label='선호분야(예: 웹, 앱 등)')
    git_url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': '깃주소를 입력해주세요'}), label='깃허브주소')
    blog_url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': '블로그주소를 입력해주세요'}), label='블로그주소')
    email = forms.CharField(label='이메일주소')
    password = forms.CharField(widget=forms.PasswordInput, label="패스워드")
    password1 = forms.CharField(widget=forms.PasswordInput, label="패스워드확인")


    class Meta:
        model = models.User
        fields = ()


    widgets = {
            username: forms.TextInput(attrs={'placeholder':'15자 이내로 입력 가능합니다.'}),
            'email': forms.EmailInput(attrs={}),
            'password' : forms.PasswordInput(attrs={}),
        }
    labels = {
            username: '닉네임',
            'email': '이메일',
            'password': '패스워드'
        }
    
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
        entered_eniac = self.cleaned_data("entered_eniac")
        blog_url = self.cleaned_data.get("blog_url")

        user.username = username
        user.email = email
        user.git_url = git_url
        user.fav_pro_genre = fav_pro_genre
        user.major = major
        user.set_password(password)
        user.entered_eniac = entered_eniac
        user.blog_url = blog_url
        user.save()

    # 계정을 생성하는 함수
  
