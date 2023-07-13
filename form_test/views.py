from django.shortcuts import render

# Create your views here.

from django.views.generic import FormView, TemplateView
from .forms import PostForm

class InputView(FormView):
    template_name = "form_test/input.html"
    form_class = PostForm
    success_url = "/form_test/thankyou/"

class ThankyouView(TemplateView):
    template_name = "form_test/thankyou.html"
