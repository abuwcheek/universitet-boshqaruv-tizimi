from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "login",
        "full_name",
        "email",
        "phone",
        "position",
        "salary",
        "hire_date",
        "is_active",
        "is_staff",
    )

    list_display_links = (
        "id",
        "login",
        "full_name",
        "email",
    )

    list_editable = (
        "position",
        "salary",
        "is_active",
    )

    list_filter = (
        "position",
        "is_active",
    )

    search_fields = (
        "full_name",
        "login",
        "email",
        "phone",
    )

    ordering = ("id",)