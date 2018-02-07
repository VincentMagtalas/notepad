from django.contrib import admin

from .models import Note

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',               {'fields': ['note_title']}),
        ('Content', {'fields': ['note_text']}),
    ]
    list_display = ('note_title',)
    search_fields = ['note_title']

admin.site.register(Note, NoteAdmin)
