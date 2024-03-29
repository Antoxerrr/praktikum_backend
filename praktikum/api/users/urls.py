from rest_framework import routers

from api.users.views import AuthViewSet

router = routers.DefaultRouter()
router.register('auth', AuthViewSet, basename='auth')

urlpatterns = router.urls
