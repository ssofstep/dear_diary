from django.db.models import Q
from django.shortcuts import render
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

    def get_initial(self):
        initial = super().get_initial()
        initial["owner"] = self.request.user
        return initial

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


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

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET or None)
        diaries = []

        if request.GET and form.is_valid():
            query = form.cleaned_data['query']
            diaries = Note.objects.filter(Q(title__icontains=query) | Q(text__icontains=query), owner=request.user)

        return render(request, self.template_name, {'form': form, 'object_list': diaries})
