from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create 10 superusers with specified names and skip password validation'

    def handle(self, *args, **kwargs):
        names = ['sam', 'rohit', 'bikash', 'pallavi', 'apala', 'sarbu', 'ridhima', 'nibida', 'aayush', 'aditya']
        
        for name in names:
            email = f'{name}@gmail.com'
            if not User.objects.filter(username=name).exists():
                user = User.objects.create_superuser(
                    username=name,
                    email=email,
                    password=name
                )
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully created superuser: {name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Superuser {name} already exists'))
