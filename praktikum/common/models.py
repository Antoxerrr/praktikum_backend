from django.db import models


class BaseDBModel(models.Model):
    """Базовый класс моделей проекта."""

    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        abstract = True
