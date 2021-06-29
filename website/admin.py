from django.contrib import admin
from .models import Project, Tree

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'project_summary',
                    'client_name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',
                    'scientific_name']
    prepopulated_fields = {'slug': ('name',)}
