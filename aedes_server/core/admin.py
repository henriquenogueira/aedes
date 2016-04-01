from django.contrib import admin
from .models import Report, Cluster


class ReportModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'device_id', 'latitude', 'longitude',
                    'category', 'reported_at', 'has_photo', 'resolved')
    list_filter = ('category', 'resolved')

    actions = ['mark_as_resolved']

    def has_photo(self, obj):
        return obj.photo != ''

    def mark_as_resolved(self, request, queryset):
        '''Mark reports as resolved.'''
        updated = queryset.update(resolved=True)
        if updated == 1:
            message_bit = "1 ocorrência foi"
        else:
            message_bit = "%s ocorrências foram" % updated
        self.message_user(request, "%s marcadas como resolvidas." % message_bit)

    mark_as_resolved.short_description = 'Marcar como resolvido'
    has_photo.short_description = 'tem foto?'
    has_photo.boolean = True

class ClusterModelAdmin(admin.ModelAdmin):
    list_display = ('label', 'latitude', 'longitude', 'breeding_count', 'focus_count', 'suspicion_count')
    list_filter = ('label',)


admin.site.register(Report, ReportModelAdmin)
admin.site.register(Cluster, ClusterModelAdmin)
