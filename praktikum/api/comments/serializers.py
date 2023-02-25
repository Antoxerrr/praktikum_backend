from rest_framework import serializers

from comments.models import CommentTemplate


class CommentTemplateSerializer(serializers.ModelSerializer):
    """Сериализатор комментариев."""

    class Meta:
        model = CommentTemplate
        fields = ('text', 'created', 'updated')
