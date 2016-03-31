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
    '''
    Renders view of the clusters
    '''
    return render(request, 'clusters.html', {
        'clusters': sorted(Cluster.objects.all(), key=lambda c: -c.score)
    })

def latest(request):
    return render(request, 'latest.html', {
        'latest': Report.objects.all().order_by('-reported_at')[:20]
    })
