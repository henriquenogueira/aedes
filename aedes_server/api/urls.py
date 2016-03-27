from django.conf.urls import url, include
from rest_framework import routers
from .viewsets import ReportViewSet, ClusterViewSet

router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet)
router.register(r'clusters', ClusterViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
