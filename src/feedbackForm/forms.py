from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    message = forms.CharField(max_length=200)

