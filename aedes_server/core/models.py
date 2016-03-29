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
    device_id = models.CharField('ID do aparelho', max_length=255)
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
    breeding_count = models.PositiveIntegerField('criadouros', default=0)
    focus_count = models.PositiveIntegerField('foco', default=0)
    suspicion_count = models.PositiveIntegerField('suspeita', default=0)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = 'label',
        verbose_name = 'aglomerado'
        verbose_name_plural = 'aglomerados'

    @property
    def score(self):
        '''Return urgency score for the cluster'''
        count_sum = self.breeding_count + self.focus_count + self.suspicion_count
        if count_sum == 0:
            return 0

        pounds = 0.2 * self.focus_count + 0.3 * self.breeding_count + 0.5 * self.suspicion_count
        return pounds / count_sum

    def __str__(self):
        return '{} - ({}, {}) - {}'.format(self.label, self.latitude, self.longitude, self.address)
