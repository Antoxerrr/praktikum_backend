from rest_framework import routers

from api.comments.views import CommentsViewSet, ProjectsViewSet

router = routers.DefaultRouter()
router.register('templates', CommentsViewSet, basename='comments')
router.register('projects', ProjectsViewSet, basename='projects')

urlpatterns = router.urls
