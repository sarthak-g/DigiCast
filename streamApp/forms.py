from django import forms

class YouTubeForm(forms.Form):
    video = forms.FileField()
    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=30)
