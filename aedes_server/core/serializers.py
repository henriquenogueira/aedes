from rest_framework import serializers
from .models import Report, Cluster


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Tells Django how to serialize a report object.
    '''

    class Meta:
        model = Report
        fields = ('latitude', 'longitude', 'category')


class ClusterSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Tells Django how to serialize cluster object.
    '''

    class Meta:
        model = Cluster
        fields = ('label', 'latitude', 'longitude')
