from django.contrib import admin
from .models import Report


class ReportModelAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'category')
    list_filter = ('category',)


admin.site.register(Report, ReportModelAdmin)
