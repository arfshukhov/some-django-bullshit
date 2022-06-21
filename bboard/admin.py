from django.contrib import admin

from .models import Bd, Rubric
# Register your models here.


class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Rubric)
admin.site.register(Bd, BdAdmin)