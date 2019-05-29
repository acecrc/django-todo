from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ('created_at','updated_at',)  #入力項目から作成日時、更新日時を除外