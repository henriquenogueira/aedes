from django.shortcuts import render
from .models import Report, Cluster

from requests import get

def index(request):
    '''
    Renders the main map of the application
    '''
    return render(request, 'map.html', {
        'reports': Report.objects.all(),
        'clusters': Cluster.objects.all()
    })


def clusters(request):
    return render(request, 'clusters.html', {
        'clusters': sorted(Cluster.objects.all(), key=lambda c: -c.score)
    })
