import random
from datetime import datetime
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from projects.models import Project
from notices.models import Notice
from activities.models import Activity

from faker import Faker

class Command(BaseCommand):

    help = "It seeds the DB with tons of stuff"

    def handle(self, *args, **options):
        user_seeder = Seed.seeder()
        user_seeder.add_entity(User, 20, {"is_staff": False, "is_superuser": False})
        user_seeder.execute()

        users = User.objects.all()
        projects_seeder = Seed.seeder()
        projects_seeder.add_entity(
            Project,
            50,
            {
               "title": lambda x: projects_seeder.faker.text(),
               "desc": lambda x: projects_seeder.faker.text(),
               "tag": lambda x: projects_seeder.faker.word(),
               "git": lambda x: projects_seeder.faker.url(),
               "views": lambda x: random.randint(0, 30),
               "user" : lambda x: random.choice(users), 
           },
        )
        projects_seeder.execute()

        users = User.objects.all()
        notice_seeder = Seed.seeder()
        notice_seeder.add_entity(
            Notice,
            50,
            {
               "title": lambda x: projects_seeder.faker.text(),
               "desc": lambda x: projects_seeder.faker.text(),
          
           },
        )
        notice_seeder.execute()
        
        activity_seeder = Seed.seeder()
        activity_seeder.add_entity(
            Activity,
            50,
            {
               "title": lambda x: projects_seeder.faker.text(),
               "desc": lambda x: projects_seeder.faker.text(),

           },
        )
        activity_seeder.execute()









        # o comment도 추추가 

        self.stdout.write(self.style.SUCCESS(f"Everything seeded"))
