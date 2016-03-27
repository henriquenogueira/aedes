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
    data = Report.objects.all().values('latitude', 'longitude', 'category')
    X = [(d['latitude'], d['longitude']) for d in data]

    model = Birch(threshold=settings.THRESHOLD)

    # Getting metrics for each cluster
    labels = model.fit_predict(X)
    categories = [d['category'] for d in data]
    label_metrics = zip(labels, categories)

    clusters = zip(model.subcluster_labels_, model.subcluster_centers_)
    _update_clusters(clusters, label_metrics)


def _get_address(latitude, longitude):
    '''
    Reverse geocoding on the coordinates
    '''

    # Formatting coordinates
    latitude = COORDINATE_FORMAT.format(latitude)
    longitude = COORDINATE_FORMAT.format(longitude)

    # Getting data from Google
    url = GOOGLE_API_BASE_URL.format(latitude, longitude)

    # Parsing data
    response = loads(get(url).text)

    # Getting information that matters
    if 'results' in response:
        results = response['results']
        if results:
            return results[0]['formatted_address']

    return ''


def _update_clusters(clusters, label_metrics):
    '''
    Updates cluster info on the database.
    '''

    # Mapping labels to categories
    idx_categories = {}
    for label, category in label_metrics:
        idx_categories.setdefault(label, []).append(category)

    # Counting categories for each label
    counting = {}
    for label, categories in idx_categories.items():
        breeding = len(list(filter(lambda c: c == 'C', categories)))
        focuses = len(list(filter(lambda c: c == 'F', categories)))
        suspicions = len(list(filter(lambda c: c == 'S', categories)))
        counting[label] = {
            'breeding': breeding,
            'focuses': focuses,
            'suspicions': suspicions
        }

    # Cleaning database
    Cluster.objects.all().delete()

    # Creating new cluster objects
    for label, [lat, long] in clusters:
        Cluster.objects.create(
            label=label,
            latitude=lat,
            longitude=long,
            breeding_count=counting[label]['breeding'],
            focus_count=counting[label]['focuses'],
            suspicion_count=counting[label]['suspicions'],
            address=_get_address(lat, long)
        )
