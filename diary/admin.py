from django.contrib import admin
from diary.models import Note

@admin.register(Note)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'text', 'creation_date')
    list_filter = ('title', 'text',)
    search_fields = ('title', 'text')
