from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Report, Cluster
from .serializers import ReportSerializer, ClusterSerializer


class ReportViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    '''
    Viewset that exposes the Reports on a REST API.
    '''
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ClusterViewSet(GenericViewSet, ListModelMixin):
    '''
    Viewset that exposes the Clusters on a REST API.
    '''
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer


