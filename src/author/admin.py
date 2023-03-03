"""
Функции панели управления для приложения "Об авторе".
"""

from django.contrib import admin

from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "about",
        "resume",
        "github",
        "mail",
        "created_at",
        "updated_at",
    )

    search_fields = ("about", "resume", "github", "mail")

    list_filter = (
        "created_at",
        "updated_at",
    )
