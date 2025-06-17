from django import forms
from django.contrib.auth.models import User
from writerapp.models import BlogModel

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
        }


# class UserLoginForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['username','password']
#         widgets={
#             "username":forms.TextInput(attrs={"class":"form-control"}),
#             "password":forms.PasswordInput(attrs={"class":"form-control"}),
#         }


class UserLoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form","placeholder":"username"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form","placeholder":"password"}))
    options={
        ("reader","reader"),
        ("writer","writer")
    }
    usertype=forms.ChoiceField(choices=options,widget=forms.Select(attrs={"class":"form","placeholder":"usertype"}))


class WriterBlogForm(forms.ModelForm):
    class Meta:
        model=BlogModel
        fields=['title','description','image']
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
        }


