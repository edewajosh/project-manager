from rest_framework.serializers import ModelSerializer

from project.models import ( Project, Release, Sprint, Story, Task, DailyStandUp)

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__' 

class ReleaseSerializer(ModelSerializer):
    class Meta:
        model = Release
        fields = '__all__'

class SprintSerializer(ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'

class StorySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class DailyStandupSerializer(ModelSerializer):
    class Meta:
        model = DailyStandUp
        fields = '__all__'