from django.contrib import admin
from .models import Report, Cluster


class ReportModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'device_id', 'latitude', 'longitude',
                    'category', 'reported_at', 'has_photo')
    list_filter = ('category',)

    def has_photo(self, obj):
        print(obj.photo)
        return obj.photo != ''

    has_photo.short_description = 'tem foto?'
    has_photo.boolean = True

class ClusterModelAdmin(admin.ModelAdmin):
    list_display = ('label', 'latitude', 'longitude', 'breeding_count', 'focus_count', 'suspicion_count')
    list_filter = ('label',)


admin.site.register(Report, ReportModelAdmin)
admin.site.register(Cluster, ClusterModelAdmin)
