from django.contrib.auth import get_user_model
from django.db import models

from common.models import BaseDBModel

User = get_user_model()


class CommentTemplate(BaseDBModel):
    """Модель шаблона комментария ревьюера."""

    text = models.TextField('Текст')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='comments'
    )

    class Meta:
        verbose_name = 'Шаблон комментария'
        verbose_name_plural = 'Шаблоны комментариев'

    def __str__(self):
        return f'Комментарий ревьюера {self.user.username} <{self.pk}>'
