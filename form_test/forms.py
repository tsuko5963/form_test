from django import forms

class PostForm(forms.Form):
    name = forms.CharField(label='名前', max_length = 25)
    text = forms.CharField(label='好きな言葉', max_length = 25)

class DogCatForm(forms.Form):
    dog = forms.BooleanField(label='犬は好きですか？', required=False)
    cat = forms.BooleanField(label='猫は好きですか？', required=False)

