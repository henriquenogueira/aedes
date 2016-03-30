from django.conf import settings
from django.core.checks import Error, register


@register
def check_threshold(app_configs, **kwargs):
    '''
    Checks if THRESHOLD is set on settings.py
    '''
    errors = []
    if not hasattr(settings, 'THRESHOLD'):
        errors.append(Error(
            'settings must have the threshold for clustering',
            hint='Add THRESHOLD=0.0005 to your settings.py file',
            obj=settings,
            id='aedes.e_001'
        ))
    return errors


@register
def check_aws_credentials(app_configs, **kwargs):
    '''
    Checks if THRESHOLD is set on settings.py
    '''
    errors = []
    expected = ('AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'AWS_STORAGE_BUCKET_NAME')

    for exp in expected:
        if not hasattr(settings, exp):
            errors.append(Error(
                'settings must contain AWS credentials',
                hint='Add AWS credentials to your settings.py file',
                obj=settings,
                id='aedes.e_002'
            ))
    return errors



