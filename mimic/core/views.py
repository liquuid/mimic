from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from mimic.core import mimic_dict, mimic
from mimic.core.forms import SubmitText


def home(request):
    if request.method == "POST":
        form = SubmitText(request.POST)
        form.is_valid()
        m_dict = mimic_dict(str(form.cleaned_data['text']))
        messages.success(request, mimic(m_dict,''))
        return render(request, "index.html",
                  {'form': SubmitText({'text':str(form.cleaned_data['text'])})})

    else:
        return render(request, "index.html",
                  {'form': SubmitText()})

#def process(request):
