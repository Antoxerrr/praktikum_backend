from django.urls import path, include

from docs import swagger_urls

urlpatterns = [
    path('users/', include('api.users.urls')),
    path('comments/', include('api.comments.urls'))
] + swagger_urls()
