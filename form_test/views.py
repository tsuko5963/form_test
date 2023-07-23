from django.shortcuts import render

# Create your views here.

from django.views.generic import FormView, TemplateView
from .forms import PostForm

class InputView(FormView):
    template_name = "form_test/input.html"
    form_class = PostForm
    success_url = "/form_test/confirm/"
    def get(self, request, *args, **kwargs):
        params = {}
        session_name = ""
        session_text = ""
        if 'name' in request.session:
            session_name = request.session["name"]
        if 'text' in request.session:
            session_text = request.session["text"]
        initial_dict = dict(name = session_name, text = session_text,)
        params["form"] = PostForm(data = initial_dict)
        return render(request, self.template_name, context=params)

class ConfirmView(TemplateView):
    template_name = "form_test/confirm.html"
    def post(self, request, *args, **kwargs):
        self.request.session["name"] = request.POST["name"] 
        self.request.session["text"] = request.POST["text"] 
        return render(request, self.template_name, context=self.kwargs)

class ThankyouView(TemplateView):
    template_name = "form_test/thankyou.html"
    def post(self, request, *args, **kwargs):
        params = {}
        if 'name' in request.session:
            params["name"] = request.session["name"]
        if 'text' in request.session:
            params["text"] = request.session["text"]
        del request.session["name"]
        del request.session["text"]
        return render(request, self.template_name, context=params)
