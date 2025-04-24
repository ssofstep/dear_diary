from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

from diary.forms import NoteForm, DiarySearchForm
from diary.models import Note


class HomeView(TemplateView):
    template_name = "diary/home.html"

class NoteListView(ListView):
    model = Note
    template_name = 'diary/note_list.html'


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'diary/note_form.html'
    success_url = reverse_lazy('diary:note_list')


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'diary/note_form.html'
    success_url = reverse_lazy('diary:note_list')


class NoteDetailView(DetailView):
    model = Note
    template_name = 'diary/note_detail.html'


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'diary/note_confirm_delete.html'
    success_url = reverse_lazy('diary:note_list')


class DiarySearchView(View):
    form_class = DiarySearchForm
    template_name = 'diary/diary_search_form.html'
