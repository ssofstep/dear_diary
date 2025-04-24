from django.urls import path
from django.views.decorators.cache import cache_page


from diary.views import HomeView, NoteDeleteView, NoteDetailView, NoteUpdateView, NoteListView, NoteCreateView, DiarySearchView

app_name = 'diary'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('note/list', NoteListView.as_view(), name='note_list'),
]