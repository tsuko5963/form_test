from django.shortcuts import render

# Create your views here.

from django.views.generic import FormView, TemplateView
from .forms import PostForm

class InputView(FormView):
    template_name = "form_test/input.html"
    form_class = PostForm
    success_url = "/form_test/confirm/"

class ConfirmView(TemplateView):
    template_name = "form_test/confirm.html"
    def post(self, request, *args, **kwargs):
        self.kwargs["name"] = request.POST["name"] 
        self.kwargs["text"] = request.POST["text"] 
        return render(request, self.template_name, context=self.kwargs)

class ThankyouView(TemplateView):
    template_name = "form_test/thankyou.html"
    def post(self, request, *args, **kwargs):
        self.kwargs["name"] = request.POST["name"] 
        self.kwargs["text"] = request.POST["text"] 
        return render(request, self.template_name, context=self.kwargs)
