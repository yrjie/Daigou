from django.contrib import admin
from models import Note, Product, UserProfile

class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'pub_date', 'title', 'body')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('key', 'name', 'description', 'owner', 'price', 'date', 'like')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )

admin.site.register(Note, NoteAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
