from django.conf.urls import url, include
from rest_framework import routers
from .viewsets import ReportViewSet

router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
