from django.contrib import admin
from .models import Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head')
    search_fields = ('name', 'head__username')
    
    
admin.site.register(Department, DepartmentAdmin)
