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

    username = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'placeholder': '이름을 입력해주세요'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': '아이디'}))
    password = forms.CharField(widget=forms.PasswordInput())
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    git_url = forms.URLField(max_length=200)
   
    fav_pro_genre = forms.ChoiceField(choices=models.User._meta.get_field('fav_pro_genre').choices)
    major = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': '학과를 입력해주세요'}))
    entered_eniac = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '에니악 기수를 입력해주세요(2021년도 -> 31기)'}))  
    eniac_code = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '에니악코드 4자리를 입력해주세요'}))

    class Meta:
        model = models.User
        fields = ("username",
"email",
"password",
"password1",
"git_url",
"fav_pro_genre",
"major",
"entered_eniac",
"eniac_code",)

    def clean_eniac_code(self):
        aniac_code = self.cleaned_data.get("eniac_code")
        if(aniac_code == "4123"):
            return aniac_code
        else:
            raise forms.ValidationError("Does not match the Aniac code")
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
        
        username = self.cleaned_data("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        git_url = self.cleaned_data("git_url")
        fav_pro_genre = self.cleaned_data("fav_pro_genre")
        major = self.cleaned_data("major")
        entered_eniac = self.cleaned_data("entered_eniac")
        eniac_code = self.cleaned_data("eniac_code")
      
        user = models.User.objects.create_user(username, email, password)
        # 왜..?
       
        user.username = username
        user.email = email
        user.password = password
        user.git_url = git_url
        user.fav_pro_genre = fav_pro_genre
        user.major = major
        user.entered_eniac = entered_eniac
        user.eniac_code = eniac_code

        
        user.save()






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