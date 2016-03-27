from json import loads

from django.conf import settings
from requests import get
from sklearn.cluster import Birch
from .models import Report, Cluster

COORDINATE_FORMAT = '{0:.6f}'
GOOGLE_API_BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}'

def compute_clusters():
    '''
    Calculates the centroid centers based on the reports
    on the database.
    '''
    data = Report.objects.all().values('latitude', 'longitude')
    X = [list(d.values()) for d in data]

    model = Birch(threshold=settings.THRESHOLD)
    model.fit(X)

    clusters = zip(model.subcluster_labels_, model.subcluster_centers_)
    _update_clusters(clusters)


def _get_address(latitude, longitude):
    '''
    Reverse geocoding on the coordinates
    '''

    # Formatting coordinates
    latitude = COORDINATE_FORMAT.format(latitude)
    longitude = COORDINATE_FORMAT.format(longitude)

    # Getting data from Google
    url = GOOGLE_API_BASE_URL.format(longitude, latitude)

    # Parsing data
    response = loads(get(url).text)

    # Getting information that matters
    if 'results' in response:
        results = response['results']
        if results:
            return results[0]['formatted_address']

    return ''


def _update_clusters(clusters):
    '''
    Updates cluster info on the database.
    '''
    Cluster.objects.all().delete()
    for label, [lat, long] in clusters:
        Cluster.objects.create(
            label=label,
            latitude=lat,
            longitude=long,
            address=_get_address(lat, long)
        )
