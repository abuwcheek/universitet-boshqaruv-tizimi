from django.contrib import admin

# Register your models here.
from .models import Faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at', 'is_active', 'is_deleted')
    list_filter = ('is_active', 'is_deleted')
    list_editable = ('is_active', 'is_deleted')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)