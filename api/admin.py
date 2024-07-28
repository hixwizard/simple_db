from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Project, Task, Comment, User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'avatar', 'role'
    )
    search_fields = ('username', 'email')
    list_display_links = ('username',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'start_time', 'end_time', 'file'
    )
    list_display_links = ('title',)


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'project', 'title', 'description', 'start_date',
        'end_date', 'priority', 'assignee'
    )
    list_display_links = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'author', 'text')
    list_display_links = ('text',)


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
