from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import FeedbackModel
# Create your views here.

from .forms import FeedbackForm


def feedback_form(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FeedbackForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_form_entry = FeedbackModel()
            new_form_entry.name = form.cleaned_data['name']
            new_form_entry.email = form.cleaned_data['email']
            new_form_entry.message = form.cleaned_data['message']

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            new_form_entry.save()
            return render(request, "feedbackSubmitted.html", {"form": form})
        else:
            raise ValidationError(_('Invalid Entries'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = FeedbackForm()
        return render(request, "feedback.html", {"form": form})
