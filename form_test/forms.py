from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

class PostForm(forms.Form):
    date = forms.DateField(
        label="日付",
        widget=DatePickerInput(
                format='%Y-%m-%d'  #formに入る日付の書式を指定
                ,options={
                    'locale': 'ja' #言語を指定
                    ,'dayViewHeaderFormat': 'YYYY年 MMMM', #カレンダーの日付の表示書式を指定
                })
    )
    name = forms.CharField(label='名前', max_length = 25)
    text = forms.CharField(label='好きな言葉', max_length = 25)

class DogCatForm(forms.Form):
    dog = forms.BooleanField(label='犬は好きですか？', required=False)
    cat = forms.BooleanField(label='猫は好きですか？', required=False)

