from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.comments.serializers import CommentTemplateSerializer


class CommentsViewSet(ModelViewSet):
    """ViewSet шаблонов комментариев."""

    permission_classes = (IsAuthenticated,)
    serializer_class = CommentTemplateSerializer

    def get_queryset(self):
        return self.request.user.comments.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
