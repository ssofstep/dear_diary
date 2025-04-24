from django.forms import ModelForm
from django import forms
from diary.models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        exclude = ['owner']


class DiarySearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Поиск'}))
