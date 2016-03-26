from django.conf import settings
from sklearn.cluster import Birch
from .models import Report, Cluster


def compute_clusters():
    '''
    Calculates the centroid centers based on the reports
    on the database.
    '''
    data = Report.objects.all().values('latitude', 'longitude')
    X = [list(d.values()) for d in data]

    model = Birch(threshold=settings.THRESHOLD)
    model.fit(X)

    return zip(model.subcluster_labels_, model.subcluster_centers_)


def update_clusters(clusters):
    '''
    Updates cluster info on the database.
    '''
    Cluster.objects.all().delete()
    for label, [lat, long] in clusters:
        Cluster.objects.create(
            label=label,
            latitude=lat,
            longitude=long,
        )
