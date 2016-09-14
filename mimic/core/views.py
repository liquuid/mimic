from django.shortcuts import render

from mimic.core.forms import SubmitText


def home(request):
    return render(request, "index.html",
                  {'form': SubmitText()})

#def process(request):
