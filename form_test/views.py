from django.shortcuts import render

# Create your views here.

from django.views.generic import FormView, TemplateView
from .forms import PostForm, DogCatForm

class InputView(FormView):
    template_name = "form_test/input.html"
    form_class = PostForm
    success_url = "/form_test/input2/"
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

class Input2View(FormView):
    template_name = "form_test/input2.html"
    success_url = "/form_test/confirm/"
    def get(self, request, *args, **kwargs):
        params = {}
        session_dog = ""
        session_cat = ""
        if 'dog' in request.session:
            session_dog = request.session["dog"]
        if 'cat' in request.session:
            session_cat = request.session["cat"]
        initial_dict = dict(dog = session_dog, cat = session_cat,)
        params["form"] = DogCatForm(data = initial_dict)
        return render(request, self.template_name, context=params)

    def post(self, request, *args, **kwargs):
        params = {}
        session_dog = ""
        session_cat = ""
        request.session["name"] = request.POST["name"] 
        request.session["text"] = request.POST["text"] 
        if 'dog' in request.session:
            session_dog = request.session["dog"]
        if 'cat' in request.session:
            session_cat = request.session["cat"]
        initial_dict = dict(dog = session_dog, cat = session_cat,)
        params["form"] = DogCatForm(data = initial_dict)
        return render(request, self.template_name, context=params)

class ConfirmView(TemplateView):
    template_name = "form_test/confirm.html"
    def post(self, request, *args, **kwargs):
        params = {}
        if('dog' in request.POST):
            request.session["dog_text"] = '犬が好きです。' 
            request.session["dog"] = request.POST["dog"] 
        else:
            request.session["dog_text"] = '犬が好きではありません。' 
            if 'dog' in request.session:
                del request.session["dog"]
        if('cat' in request.POST):
            request.session["cat_text"] = '猫が好きです。' 
            request.session["cat"] = request.POST["cat"] 
        else:
            request.session["cat_text"] = '猫が好きではありません。' 
            if 'cat' in request.session:
                del request.session["cat"]
        return render(request, self.template_name, context=self.kwargs)

class ThankyouView(TemplateView):
    template_name = "form_test/thankyou.html"
    def post(self, request, *args, **kwargs):
        params = {}
        if 'name' in request.session:
            params["name"] = request.session["name"]
            del request.session["name"]
        if 'text' in request.session:
            params["text"] = request.session["text"]
            del request.session["text"]
        if 'dog' in request.session:
            del request.session["dog"]
        if 'cat' in request.session:
            del request.session["cat"]
        params["dog"] = request.session["dog_text"]
        params["cat"] = request.session["cat_text"]
        del request.session["dog_text"]
        del request.session["cat_text"]
        return render(request, self.template_name, context=params)
