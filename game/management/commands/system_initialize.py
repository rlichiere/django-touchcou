
import sys

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):

        # populate default db data if don't exists
        pass

        # end
        print('system_initialize: End.\n')
        sys.exit(0)
