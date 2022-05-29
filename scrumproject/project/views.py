from rest_framework.viewsets import ModelViewSet

from project.models import (Project, Release, Sprint, Story, Task, DailyStandUp)
from project.serializers import (DailyStandupSerializer, ProjectSerializer, ReleaseSerializer, SprintSerializer, StorySerializer, TaskSerializer)

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ReleaseViewSet(ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer

class SprintViewSet(ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer

class StoryViewSet(ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DailyStandupViewSet(ModelViewSet):
    queryset = DailyStandUp.objects.all()
    serializer_class = DailyStandupSerializer




