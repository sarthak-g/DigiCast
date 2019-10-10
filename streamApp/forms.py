from django import forms

class YouTubeForm(forms.Form):
    video = forms.FileField()
