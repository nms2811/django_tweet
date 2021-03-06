from django import forms


from .models import Tweet

MAX_TWEET_LENGTH = 240

class TweetForm(forms.ModelForm):
    content = forms.CharField()
    class Meta:
        # describing forms
        model = Tweet
        fields = ['content']
    
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("This Tweet is too long")
        return content