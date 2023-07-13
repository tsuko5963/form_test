from django import forms
from .models import PostModel

class PostForm(forms.ModelForm):
    class Meta():
        model = PostModel
        fields = ('name', 'text')
        labels = {'name':'名前',
                  'text':'好きな言葉',
        }
