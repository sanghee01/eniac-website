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
    # username = forms.CharField(help_text=False, widget=forms.TextInput(attrs={'placeholder': '이름을 입력해주세요'}), label='이름')
    # major = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '전공을 입력해주세요'}), label='전공')

    # entered_eniac = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '기수를 입력해주세요'}), label='에니악기수')
    # fav_pro_genre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '선호분야를 입력해주세요'}), label='선호분야(예: 웹, 앱 등)')
    # git_url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': '깃주소를 입력해주세요'}), label='깃허브주소')
    # blog_url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': '블로그주소를 입력해주세요'}), label='블로그주소')
    # email = forms.CharField(label='이메일주소')
    # password = forms.CharField(widget=forms.PasswordInput, label="패스워드")
    # password1 = forms.CharField(widget=forms.PasswordInput, label="패스워드확인")

    password1 = forms.CharField(widget=forms.PasswordInput, label="패스워드확인")
    class Meta:
        model = models.User
        fields = ("username", "major", "student_id", "phone_number", "entered_eniac", "email", "password")

        widgets = {
            "username": forms.TextInput(attrs={'placeholder': '이름을 입력해주세요'}),
            "major": forms.TextInput(attrs={'placeholder': '전공을 입력해주세요'}),
            "entered_eniac": forms.TextInput(attrs={'placeholder': '기수를 입력해주세요'}),

            "student_id": forms.TextInput(attrs={'placeholder': '학번을 입력해주세요'}),
            "phone_number": forms.TextInput(attrs={'placeholder': '전화번호를 입력해주세요'}),
         
         
            "password": forms.PasswordInput,
            "password1": forms.PasswordInput,
        }
        labels = {
            "username": "이름",
            "major": "전공",
            "entered_eniac": "에니악기수", 


            "student_id": "학번",
            "phone_number": "전화번호",

         
            "email": "이메일", 
            "password": "패스워드", 
            "password1":"패스워드 확인",
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
            msg = u"비밀번호가 틀립니다"
            raise forms.ValidationError(msg)
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
        entered_eniac = self.cleaned_data.get("entered_eniac")
        blog_url = self.cleaned_data.get("blog_url")

        student_id = self.cleaned_data("student_id")
        phone_number = self.cleaned_data("phone_number")

        user.studend_id = student_id
        user.phone_number = phone_number
        user.username = username
        user.email = email     
        user.major = major
        user.set_password(password)
        user.entered_eniac = entered_eniac
        user.save()

    # 계정을 생성하는 함수
  
class SignUpSecForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = ("git_url", "blog_url", "fav_pro_genre")

        widgets = {
            "git_url": forms.TextInput(attrs={'placeholder': '깃주소를 입력해주세요'}),
            "blog_url": forms.TextInput(attrs={'placeholder': '블로그주소를 입력해주세요'}),
            "fav_pro_genre": forms.TextInput(attrs={'placeholder': '선호분야를 입력해주세요'}),
        }
        labels = {
            "git_url": "깃주소", 
            "blog_url": "블로그주소", 
            "fav_pro_genre": "좋아하는 장르", 
        }

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        
        git_url = self.cleaned_data.get("git_url")
        fav_pro_genre = self.cleaned_data.get("fav_pro_genre")        
        blog_url = self.cleaned_data.get("blog_url")

        user.git_url = git_url
        user.fav_pro_genre = fav_pro_genre
        user.blog_url = blog_url
        user.save()
