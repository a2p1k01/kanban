from django.contrib import admin
from .models import Issue


# Register your models here.
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'author', 'created']
    list_filter = ['status', 'created', 'author']
    search_fields = ['title', 'status']
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ['author']
    date_hierarchy = 'created'
    ordering = ['status', 'created']
