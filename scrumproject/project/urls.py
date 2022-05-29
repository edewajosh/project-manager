from rest_framework.routers import DefaultRouter

from project.views import (DailyStandupViewSet, ProjectViewSet, ReleaseViewSet, SprintViewSet, StoryViewSet, TaskViewSet)

router = DefaultRouter()
router.register(r'project', ProjectViewSet)
router.register(r'release', ReleaseViewSet)
router.register(r'sprint', SprintViewSet)
router.register(r'story', StoryViewSet)
router.register(r'task', TaskViewSet)
router.register(r'daily-stand-up', DailyStandupViewSet)

urlpatterns = router.urls