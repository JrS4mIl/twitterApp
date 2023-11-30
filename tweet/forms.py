from django import forms
from .models import Tweet
class AddTweetForm(forms.Form):
    nickname_input=forms.CharField(label='Nickname',max_length=50)
    message_input=forms.CharField(label='Message',max_length=100,
                                  widget=forms.Textarea(attrs={"class":"tweetmessage"}))

class AddTweetModelForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['nickname','message']

