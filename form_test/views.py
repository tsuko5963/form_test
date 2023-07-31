from django.shortcuts import render

# Create your views here.

from django.views.generic import FormView, TemplateView, ListView, DetailView
from .forms import PostForm, DogCatForm
from .models import PostDogCatModel

class InputView(FormView):
    template_name = "form_test/input.html"
    form_class = PostForm
    success_url = "/form_test/input2/"
    def get(self, request, *args, **kwargs):
        params = {}
        session_date = ""
        session_name = ""
        session_text = ""
        if 'date' in request.session:
            session_date = request.session["date"]
        if 'name' in request.session:
            session_name = request.session["name"]
        if 'text' in request.session:
            session_text = request.session["text"]
        initial_dict = dict(date = session_date, name = session_name, text = session_text,)
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
        request.session["date"] = request.POST["date"] 
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
        param_dog = False
        param_cat = False
        if 'date' in request.session:
            params["date"] = request.session["date"]
            del request.session["date"]
        if 'name' in request.session:
            params["name"] = request.session["name"]
            del request.session["name"]
        if 'text' in request.session:
            params["text"] = request.session["text"]
            del request.session["text"]
        if 'dog' in request.session:
            del request.session["dog"]
            param_dog = True
        if 'cat' in request.session:
            del request.session["cat"]
            param_cat = True
        params["dog"] = request.session["dog_text"]
        params["cat"] = request.session["cat_text"]
        del request.session["dog_text"]
        del request.session["cat_text"]
        record = PostDogCatModel(date = params["date"], name = params["name"], text = params["text"], dog = param_dog, cat = param_cat)
        record.save()
        return render(request, self.template_name, context=params)

class IndexView(ListView):
    template_name = "form_test/index.html"
    context_object_name = "post_list"

    def get_queryset(self):
        return PostDogCatModel.objects.all()

class DetailView(DetailView):
    model = PostDogCatModel
    template_name = "form_test/detail.html"
