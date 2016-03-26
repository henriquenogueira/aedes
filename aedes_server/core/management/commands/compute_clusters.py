from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Calculate clusters for AedeSpot app'

    def add_arguments(self, parser):
        # Optional: set the number of clusters
        parser.add_argument('n_clusters', nargs='?', type=int, default=None,
                            help='specifies number of clusters')

    def handle(self, *args, **options):
        raise NotImplementedError('Not implemented yet')
