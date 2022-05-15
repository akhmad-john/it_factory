from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name',)
