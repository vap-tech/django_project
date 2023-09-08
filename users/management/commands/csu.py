from django.core.management import BaseCommand

from users.models import User, Country


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@v-petrenko.ru',
            first_name='Fox',
            last_name='Kot',
            country=Country.objects.first(),
            is_staff=True,
            is_superuser=True,
        )
        user.set_password('os.getenv')
        user.save()
