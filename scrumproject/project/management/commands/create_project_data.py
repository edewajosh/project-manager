from platform import release
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from datetime import datetime

import random

from project.models import (Project, Release)

class Command(BaseCommand):

    help = 'Create/populate models with random data'

    def add_arguments(self, parser) -> None:
        # Positional arguments
        parser.add_argument('total', type=int, help='Indicates the number of data models to be created')
        
        # Named (optional) arguments
        parser.add_argument('-p', '--project', action='store_true', help='Create project models')

        parser.add_argument('-R', '--release',  action='store_true', help='Create release objects')

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

