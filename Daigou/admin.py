from django.contrib import admin
from models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'pub_date', 'title', 'body')

admin.site.register(Note, NoteAdmin)