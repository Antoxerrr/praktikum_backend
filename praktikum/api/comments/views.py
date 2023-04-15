from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.comments.serializers import CommentTemplateSerializer, \
    GetProjectSerializer, CreateEditCommentTemplateSerializer
from comments.models import Project


class CommentsViewSet(ModelViewSet):
    """ViewSet шаблонов комментариев."""

    permission_classes = (IsAuthenticated,)
    serializer_class = CommentTemplateSerializer

    def get_queryset(self):
        return self.request.user.comments.order_by('-created')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return CreateEditCommentTemplateSerializer
        return self.serializer_class


class ProjectsViewSet(ReadOnlyModelViewSet):
    """ViewSet проектов."""

    permission_classes = (IsAuthenticated,)
    serializer_class = GetProjectSerializer
    queryset = Project.objects
