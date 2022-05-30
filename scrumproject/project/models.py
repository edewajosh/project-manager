from django.conf import settings
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=254)
    date_started = models.DateTimeField(auto_now_add=True, null=False)
    description = models.TextField()

class Release(models.Model):

    name = models.CharField(max_length=254)
    project = models.ForeignKey(
                                Project,
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE,
                                related_name='release'
                            )
    release_date = models.DateTimeField(auto_now_add=True, null=False)
    description = models.TextField()

class Sprint(models.Model):
    name = models.CharField(max_length=254)
    starts_on = models.DateField()
    ends_on = models.DateField()
    project = models.ForeignKey(Project, verbose_name='project_assigned', on_delete=models.CASCADE)
    release = models.ForeignKey(Release, 
                                verbose_name='release_assigned',
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE)

class Story(models.Model):
    description = models.TextField()
    sprint = models.ForeignKey(Sprint,
                            verbose_name='sprint_assigned',
                            blank=True,
                            null=True,
                            on_delete=models.CASCADE)
    developer = models.ForeignKey(settings.AUTH_USER_MODEL, 
                            blank=True,
                            null=True,
                            on_delete=models.CASCADE)
    deployed = models.BooleanField(default=False)
    points = models.PositiveIntegerField()

    class Meta:
        verbose_name='Story'
        verbose_name_plural='Stories'

class Task(models.Model):
    story = models.ForeignKey(Story, verbose_name='story_assigned', on_delete=models.CASCADE)
    built = models.BooleanField(default=False)
    tested = models.BooleanField(default=False)

class DailyStandUp(models.Model):
    project = models.ForeignKey(
                                Project,
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE
                            )
    sprint = models.ForeignKey(Sprint,
                            verbose_name='sprint_assigned',
                            blank=True,
                            null=True,
                            on_delete=models.CASCADE)
    happened_on = models.DateField()


class Retrospective(models.Model):
    pass