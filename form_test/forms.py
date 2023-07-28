from django import forms
from .models import PostModel, DogCatModel

class PostForm(forms.ModelForm):
    class Meta():
        model = PostModel
        fields = ('name', 'text')
        labels = {'name':'名前',
                  'text':'好きな言葉',
        }

class DogCatForm(forms.Form):
    dog = forms.BooleanField(label='犬は好きですか？', required=False)
    cat = forms.BooleanField(label='猫は好きですか？', required=False)

