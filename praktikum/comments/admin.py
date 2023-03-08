from django.contrib import admin

from comments.models import Project, CommentTemplate

admin.site.register(CommentTemplate)
admin.site.register(Project)
