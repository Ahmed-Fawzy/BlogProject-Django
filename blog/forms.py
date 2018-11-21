from django import forms
from django.db import connection

from .models import User, Post, Permission
from django.contrib.admin.widgets import FilteredSelectMultiple



class Login_Form(forms.ModelForm):

    class Meta:
        model = User
        fields = ['user_name', 'user_pass']
        labels = {'user_name': '', 'user_pass': ''}
        widgets = {'user_pass': forms.PasswordInput(attrs= {'placeholder': 'Password'})}


class Post_Form(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', 'published']
        labels = {'title': 'Title', 'body': 'Content'}
        widgets = {'title': forms.TextInput(attrs= {'placeholder': 'Title',"class":"form-control" }),
                   'body': forms.Textarea( attrs={'placeholder': 'Content', "class": "form-control"}),
                   'published': forms.HiddenInput()
                   }




class Add_User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'user_pass', 'user_email', 'permission']
        labels = {'user_name': 'Username', 'user_pass': 'Password', 'user_email':'Email' , 'permission':'Permission'}
        widgets = {'user_name': forms.TextInput(attrs= {'placeholder': 'Username',"class":"form-control" }),
                    'user_pass': forms.PasswordInput(attrs={'placeholder': 'Password',"class":"form-control" }),
                   'user_email': forms.TextInput(attrs={'placeholder': 'Email', "class": "form-control"}),
                    'permission': forms.SelectMultiple(attrs={"class":"form-control col-4"})


                           }

        #filter_horizontal = ('permission',)



        #labels = {'user_name': '', 'user_pass': ''}
        #widgets = {'user_pass': forms.PasswordInput(attrs= {'placeholder': 'Password'})}















#    user_name = forms.CharField(required=True)
#    user_pass = forms.CharField(widget=forms.PasswordInput)