from django.contrib import admin
from .models import Issue


# Register your models here.
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'author', 'created', 'status']
    list_filter = ['status', 'created', 'author', 'type']
    search_fields = ['title', 'type', 'status']
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ['author']
    date_hierarchy = 'created'
    ordering = ['type', 'created', 'status']
