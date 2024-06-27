from django.contrib import admin
from .models import Meeting

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'host', 'start_time', 'end_time')
    list_filter = ('start_time', 'end_time', 'host')
    search_fields = ('title', 'description', 'host__username')
    filter_horizontal = ('participants',)
    date_hierarchy = 'start_time'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

