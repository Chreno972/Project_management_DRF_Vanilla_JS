from django.contrib import admin
from .models import Task, Project, Material


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'related_project')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'state',
        'github_link',
        'website_link',
    )


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'project_type',
        'related_project',
        'usability_level'
    )
