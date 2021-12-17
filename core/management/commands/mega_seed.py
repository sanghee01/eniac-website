import random
from datetime import datetime
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from projects.models import Project
from notices.models import Notice
from activities.models import Activity
from challenges.models import Challenge
from challenges.models import Challenge_Comment
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
            150,
            {
               "title": lambda x: projects_seeder.faker.text(),
               "desc": lambda x: projects_seeder.faker.text(),
               "tag": lambda x: projects_seeder.faker.words(),
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
            150,
            {
               "title": lambda x: projects_seeder.faker.text(),
               "desc": lambda x: projects_seeder.faker.text(),
               "tag": lambda x: projects_seeder.faker.words(),
           },
        )
        notice_seeder.execute()
        
        activity_seeder = Seed.seeder()
        activity_seeder.add_entity(
            Activity,
            150,
            {
               "title": lambda x: projects_seeder.faker.text(),
               "desc": lambda x: projects_seeder.faker.text(),
               
           },
        )
        activity_seeder.execute()


        challenge_seeder = Seed.seeder()
        challenge_seeder.add_entity(
            Challenge,
            150,
            {
               "users" : lambda x: random.choice(users), 
               "desc": lambda x: projects_seeder.faker.text(), 
           },
        )
        challenge_seeder.execute()







        # o comment도 추추가 

        self.stdout.write(self.style.SUCCESS(f"Everything seeded"))
