from rest_framework import serializers

from comments.models import CommentTemplate, Project


class GetProjectSerializer(serializers.ModelSerializer):
    """Сериализатор проектов."""

    class Meta:
        model = Project
        fields = ('id', 'name')


class CommentTemplateSerializer(serializers.ModelSerializer):
    """Сериализатор комментариев."""

    project = GetProjectSerializer()

    class Meta:
        model = CommentTemplate
        fields = ('id', 'text', 'created', 'updated', 'project')


class CreateEditCommentTemplateSerializer(serializers.ModelSerializer):
    """Сериализатор создания/редактирования комментариев."""

    class Meta:
        model = CommentTemplate
        fields = ('text', 'project')
