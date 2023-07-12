from django.shortcuts import render

# Create your views here.

from django.views.generic import FormView

class InputView(FormView):
    template_name = "form_test/input.html"
    form_class = PostForm
    success_url = "/confirm/"

class ConfirmView(TemplateView):
    def post(self, request):
        if request.method == "POST":
            self.params["form"] = PostForm(request.POST)
        if self.params["form"].is_valid():
            return render(request, "form_test/confirm.html", context = self.params)
        return render(request, "form_test/input.html", context = self.params)
