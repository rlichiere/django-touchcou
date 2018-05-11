
import sys

from django.core.management.base import BaseCommand

from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        # create superuser if don't exists
        if User.objects.filter(username='admin').count() < 1:
            admin_user = User(username='admin', email='admin@dev.local', password='manager')
            admin_user.save()
            print('system_initialize: admin created.')
        else:
            print('system_initialize: admin already exists.')

        # populate default db data if don't exists
        pass

        # end
        print('system_initialize: End.\n')
        sys.exit(0)
