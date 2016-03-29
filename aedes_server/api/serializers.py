from aedes_server.core.models import Report, Cluster
from rest_framework import serializers


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Tells Django how to serialize a report object.
    '''

    class Meta:
        model = Report
        fields = ('latitude', 'longitude', 'category', 'device_id')


class ClusterSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Tells Django how to serialize cluster object.
    '''

    class Meta:
        model = Cluster
        fields = ('label', 'latitude', 'longitude', 'address', 'focus_count', 'breeding_count', 'suspicion_count')
