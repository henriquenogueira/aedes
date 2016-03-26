from django.contrib import admin
from .models import Report, Cluster


class ReportModelAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'category')
    list_filter = ('category',)


class ClusterModelAdmin(admin.ModelAdmin):
    list_display = ('label', 'latitude', 'longitude')
    list_filter = ('label',)


admin.site.register(Report, ReportModelAdmin)
admin.site.register(Cluster, ClusterModelAdmin)
