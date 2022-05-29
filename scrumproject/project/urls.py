from rest_framework.routers import DefaultRouter

from project.views import ProjectViewSet

router = DefaultRouter()
router.register(r'project', ProjectViewSet)

urlpatterns = router.urls