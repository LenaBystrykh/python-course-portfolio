"""
Модели для приложения "Author" (автор портфолио).
"""


from django.db import models

from base.models import TimeStampMixin


class Author(TimeStampMixin):
    """
    Модель для хранения данных об авторе.
    """

    about = models.TextField(
        max_length=500,
        verbose_name="Описание",
        help_text="Информация об авторе",
    )
    resume = models.CharField(
        max_length=255,
        verbose_name="Резюме",
        help_text="Ссылка на резюме",
    )
    github = models.CharField(
        max_length=255,
        verbose_name="GitHub",
        help_text="Ссылка на GitHub",
    )
    mail = models.CharField(
        max_length=255,
        verbose_name="e-mail",
        help_text="e-mail адрес",
    )

    class Meta:
        verbose_name = "Обо мне"
        verbose_name_plural = "Обо мне"

    def __str__(self) -> str:
        return f'Объект "Об авторе" (id={self.pk})'
