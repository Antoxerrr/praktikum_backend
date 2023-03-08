from django.contrib.auth import get_user_model
from django.db import models

from common.models import BaseDBModel

User = get_user_model()


class Project(BaseDBModel):
    """Модель проекта, для которого актуален комментарий."""

    name = models.CharField('Название', max_length=256)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'Проект {self.name}'


class CommentTemplate(BaseDBModel):
    """Модель шаблона комментария ревьюера."""

    text = models.TextField('Текст')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='comments'
    )
    project = models.ForeignKey(
        Project,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='comments'
    )

    class Meta:
        verbose_name = 'Шаблон комментария'
        verbose_name_plural = 'Шаблоны комментариев'

    def __str__(self):
        return f'Комментарий ревьюера {self.user.username} <{self.pk}>'
