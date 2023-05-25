from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from .forms import FeedbackForm


def feedback_form(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FeedbackForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = FeedbackForm()

    return render(request, "feedback.html", {"form": form})
