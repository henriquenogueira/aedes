from django.contrib import admin
from .models import Report, Cluster


class ReportModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'category')
    list_filter = ('category',)


class ClusterModelAdmin(admin.ModelAdmin):
    list_display = ('label', 'latitude', 'longitude', 'breeding_count', 'focus_count', 'suspicion_count')
    list_filter = ('label',)


admin.site.register(Report, ReportModelAdmin)
admin.site.register(Cluster, ClusterModelAdmin)
