from django.urls import path

from rest_framework.routers import DefaultRouter
from user.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

admin_detail=UserViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })

urlpatterns = [
    path('admin/<int:admin>', admin_detail, name='admin-detail'),
]
urlpatterns += router.urls