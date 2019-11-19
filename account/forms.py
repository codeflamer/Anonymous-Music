from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class RegistrationForm(UserCreationForm):
    email= forms.EmailField(required=True)
    class Meta:
        model = User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

    def save(self,commit=True):
        user = super(RegistrationForm  ,self).save(commit=False)
        user.first_name= self.cleaned_data['first_name']
        user.last_name= self.cleaned_data['last_name']
        user.email= self.cleaned_data['email']

        if commit:
            user.save()
        return user

class UpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password'
        ]


# class UserForm(forms.ModelForm):
#
#     password= forms.CharField(widget=forms.PasswordInput)
#     confirmpassword = forms.CharField(widget=forms.PasswordInput)
#     email=forms.EmailField(required=True)
#     class Meta:
#         model = User
#         fields=['username','email','password','confirmpassword']
#
#     def clean_username(self):
#         urn=self.cleaned_data.get('username')
#         qs = User.objects.filter(username=urn)
#         if qs.exists():
#             raise forms.ValidationError('Username already exists.')
#
#     def clean_email(self):
#         email=self.cleaned_data.get('email')
#         if email == '':
#             raise forms.ValidationError('This Field is required')