from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from datetime import datetime, date

import random

from project.models import (DailyStandUp, Project, Release, Sprint, Story, Task)
from user.models import User

class Command(BaseCommand):

    help = 'Create/populate models with random data'

    def add_arguments(self, parser) -> None:
        # Positional arguments
        parser.add_argument('total', type=int, help='Indicates the number of data models to be created')
        
        # Named (optional) arguments
        parser.add_argument('-P', '--project', action='store_true', help='Create project models')

        parser.add_argument('-R', '--release',  action='store_true', help='Create release objects')

        parser.add_argument('-S', '--sprint', action='store_true', help='Create sprint objects')

        parser.add_argument('-Y', '--story', action='store_true', help='Create story objects')

        parser.add_argument('-T', '--task', action='store_true', help='Create Task objects')

        parser.add_argument('-D', '--standup', action='store_true', help='Create DailyStandup objects')

    def handle(self, *args, **options):
        if options['project']:
            for i in range(options['total']):
                name = get_random_string(50)
                description = get_random_string(1000)
                Project.objects.create(name=name, description=description, date_started=datetime.now())
        if options['release']:
            project_keys = [ proj for proj in Project.objects.all()]
            for i in range(options['total']):
                name = get_random_string(50)
                description = get_random_string(1000)
                project = random.choice(project_keys)
                Release.objects.create(name=name, project=project, description=description, release_date=datetime.now())

        if options['sprint']:
            project_keys = [ proj for proj in Project.objects.all()]
            releases = [ release for release in Release.objects.all()]
            for i in range(options['total']):
                name = get_random_string(50)
                project = random.choice(project_keys)
                release = random.choice(releases)
                data = datetime.today()
                starts_on = date(data.year, data.month, data.day)
                ends_on = date(data.year, data.month+1, data.day)
                Sprint.objects.create(name=name, project=project, release=release, starts_on=starts_on, ends_on=ends_on)

        if options['story']:
            sprints = [ sprint for sprint in Sprint.objects.all()]
            users = [ user for user in User.objects.all()]

            for i in range(options['total']):
                description = get_random_string(1000)
                developer = random.choice(users)
                sprint = random.choice(sprints)
                Story.objects.create(description=description, developer=developer, sprint=sprint, deployed=False, points=7)

        if options['task']:
            stories = [ story for story in Story.objects.all()]

            for i in range(options['total']):
                story = random.choice(stories)
                Task.objects.create(story=story, built=True, tested=False)

        if options['standup']:
            sprints = [ sprint for sprint in Sprint.objects.all()]
            projects = [ project for project in Project.objects.all()]

            for i in range(options['total']):
                sprint = random.choice(sprints)
                project = random.choice(projects)
                data = datetime.today()
                happened_on = date(data.year, data.month, data.day)
                DailyStandUp.objects.create(sprint=sprint, project=project, happened_on=happened_on)


