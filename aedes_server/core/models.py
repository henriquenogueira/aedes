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
        ('SD', 'Suspeita de dengue'),  # Someone near feeling symptoms of dengue
        ('SZ', 'Suspeita de zika'),  # Someone near feeling symptoms of zika
        ('SC', 'Suspeita de chikungunya'),  # Someone near feeling symptoms of chikungunya
    )

    latitude = models.FloatField('latitude')
    longitude = models.FloatField('longitude')
    photo = models.ImageField('foto', upload_to='upload/%Y/%m/%d/', blank=True)
    device_id = models.CharField('ID do aparelho', max_length=255)
    comment = models.TextField('comentário', blank=True, default='')
    category = models.CharField('categoria', max_length=2, choices=REPORT_CATEGORIES)
    resolved = models.BooleanField('resolvido', default=False)
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
