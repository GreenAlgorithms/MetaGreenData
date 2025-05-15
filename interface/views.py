from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MetaDataForm


def get_metadata(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = MetaDataForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, "thanks.html", {"form": form})
            # return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MetaDataForm()

    return render(request, "metadata.html", {"form": form})

    