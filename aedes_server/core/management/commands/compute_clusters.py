from aedes_server.core.clusters import compute_clusters
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Calculate clusters for AedeSpot app.'

    def handle(self, *args, **options):
        '''
        Computing clusters.
        '''
        compute_clusters()
