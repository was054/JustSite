from django.contrib import admin
from .models import ModelNews
from .models import Rubric

class ModelNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Rubric)
admin.site.register(ModelNews, ModelNewsAdmin)
