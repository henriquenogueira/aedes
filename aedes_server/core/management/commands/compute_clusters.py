from aedes_server.core.clusters import compute_clusters, update_clusters
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Calculate clusters for AedeSpot app'

    def handle(self, *args, **options):
        self.stdout.write('Computing cluster centers.')
        clusters = compute_clusters()

        self.stdout.write('Updating cluster information on the database.')
        update_clusters(clusters)

        self.stdout.write('Done!')
