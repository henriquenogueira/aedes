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
    category = models.CharField('category', max_length=1, choices=REPORT_CATEGORIES)
    reported_at = models.DateTimeField('reportado em', auto_now_add=True)

    def __str__(self):
        return '({}, {}) - {}'.format(self.latitude, self.longitude, self.category)
