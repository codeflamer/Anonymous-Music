from django import forms
from .models import Post,Message,Tweet

class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'write a post...'
        }
    ))
    class Meta:
        model = Post
        fields =['post']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['post']

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text']
