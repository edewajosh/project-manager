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
                                null=True
                                on_delete=models.CASCADE
                            )
    release_date = models.DateTimeField(auto_now_add=True, null=False)
    description = models.TextField()

class Sprint(models.Model):
    name = models.CharField(max_length=254)
    starts_on = models.DateField()
    ends_on = models.DateField()
    project = models.ForeignKey(Project, verbose_name='project_assigned', on_delete=models.CASCADE)
    release = models.ForeignKey(Release, 
                                verbose_name='released_assigned',
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE)