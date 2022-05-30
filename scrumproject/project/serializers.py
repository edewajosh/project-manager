from platform import release
from rest_framework.serializers import ModelSerializer

from project.models import ( Project, Release, Sprint, Story, Task, DailyStandUp)


class ReleaseSerializer(ModelSerializer):
    class Meta:
        model = Release
        fields = '__all__'
class ProjectSerializer(ModelSerializer):

    release = ReleaseSerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__' 

    def create(self, validated_data):
        project_release = validated_data.pop('release')
        project_instance = Project.objects.create(**validated_data)
        for release in project_release:
            Release.objects.create(project=project_instance, **release)
        return project_instance

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