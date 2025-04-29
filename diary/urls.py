from django.urls import path
from django.views.decorators.cache import cache_page


from diary.views import HomeView, NoteDeleteView, NoteDetailView, NoteUpdateView, NoteListView, NoteCreateView, DiarySearchView

app_name = 'diary'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('note/list', NoteListView.as_view(), name='note_list'),
    path('note/detail/<int:pk>', NoteDetailView.as_view(), name='note_detail'),
    path('note/create', NoteCreateView.as_view(), name='note_create'),
    path('note/delete/<int:pk>', NoteDeleteView.as_view(), name='note_delete'),
    path('note/update/<int:pk>', NoteUpdateView.as_view(), name='note_update'),
    path('note/search', DiarySearchView.as_view(), name='diary_search'),
]
