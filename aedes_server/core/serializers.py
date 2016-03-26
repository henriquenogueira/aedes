from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Tells Django how to serialize a report object.
    '''

    class Meta:
        model = Report
        fields = ('latitude', 'longitude', 'category')
