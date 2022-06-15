from platform import release
from rest_framework.serializers import ModelSerializer, ReadOnlyField

from project.models import ( Project, Release, Sprint, Story, Task, DailyStandUp)


class ReleaseSerializer(ModelSerializer):
    class Meta:
        model = Release
        fields = ['id', 'name', 'release_date', 'project', 'description']
        extra_kwargs = {
            'id': {'read_only': True}
        }
class ProjectSerializer(ModelSerializer):

    release = ReleaseSerializer(many=True)
    class Meta:
        model = Project
        fields = ['id', 'name', 'date_started', 'description', 'release']
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        project_release = validated_data.pop('release')
        project_instance = Project.objects.create(**validated_data)
        for release in project_release:
            Release.objects.create(project=project_instance, **release)
        return project_instance

class SprintSerializer(ModelSerializer):
    class Meta:
        model = Sprint
        fields = ['id','name', 'starts_on', 'ends_on', 'project', 'release']
        extra_kwargs = {'id': {'read_only': True}}


class StorySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ['id','description', 'developer', 'deployed', 'points']
        extra_kwargs = {
            'id': {'read_only': True}
        }

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'story', 'built', 'tested']
        extra_kwargs = {
            'id': {'read_only': True}
        }

class DailyStandupSerializer(ModelSerializer):
    class Meta:
        model = DailyStandUp
        fields = ['id', 'project', 'sprint', 'happened_on']
        extra_kwargs = {
            'id': {'read_only': True}
        }