from django import forms
from .models import FeedbackModel


class FeedbackForm(forms.Form):
    class Meta:
        model = FeedbackModel
        fields = ["fullname", "email", "message"]
        labels = {'fullname': "Name", "email": "Email", "message": "Feedback"}
