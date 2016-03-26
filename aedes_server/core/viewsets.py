from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Report
from .serializers import ReportSerializer


class ReportViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    '''
    Viewset that exposes the Reports on a REST API.
    '''
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
