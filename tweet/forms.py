from django import forms


class CreateTweetForm(forms.Form):
    tweet = forms.CharField(widget=forms.Textarea, max_length=140)
