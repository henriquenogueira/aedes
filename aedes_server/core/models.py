from django.db import models


class Report(models.Model):
    '''
    Model that represents a given report by an user.
    It contains information about the location of
    the report as well as the type and timestamp.
    '''

    REPORT_CATEGORIES = (
        ('F', 'Foco'),  # Represents a potential place where aedes can appear
        ('C', 'Criadouro'),  # Represents aedes' larva on a spot
        ('S', 'Suspeita')  # Someone near feeling symptons of aedes-transmitted diseases
    )

    latitude = models.FloatField('latitude')
    longitude = models.FloatField('longitude')
    category = models.CharField('categoria', max_length=1, choices=REPORT_CATEGORIES)
    reported_at = models.DateTimeField('reportado em', auto_now_add=True)

    class Meta:
        ordering = '-id',
        verbose_name = 'ocorrência'
        verbose_name_plural = 'ocorrências'

    def __str__(self):
        return '({}, {}) - {}'.format(self.latitude, self.longitude, self.category)


class Cluster(models.Model):
    '''
    Represents a cluster into the database.
    '''
    label = models.IntegerField('etiqueta', unique=True)
    latitude = models.FloatField('latitude')
    longitude = models.FloatField('longitude')
    address = models.CharField('endereço', max_length=512, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = 'label',
        verbose_name = 'centro de interesse'
        verbose_name_plural = 'centros de interesse'

    def __str__(self):
        return '{} - ({}, {}) - {}'.format(self.label, self.latitude, self.longitude, self.address)
