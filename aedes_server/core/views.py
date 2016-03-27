from django.shortcuts import render
from .models import Report


def index(request):
    '''
    Renders the main map of the application
    '''
    return render(request, 'map.html', {'reports': Report.objects.all()})
