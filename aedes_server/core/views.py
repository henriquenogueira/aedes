from django.shortcuts import render
from .models import Report, Cluster


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
        'clusters': Cluster.objects.all()
    })
