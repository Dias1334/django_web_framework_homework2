from django.contrib import admin

from table_link.models import Books
from table_link.models import Category


# class HomeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'author', 'janre', 'info')
#     list_display_links = ('name', 'author', )
#     ordering = ('author',)
#

# Register your models here.
admin.site.register(Books)
admin.site.register(Category)
