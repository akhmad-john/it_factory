from django.contrib import admin

from .models import Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'trade_point_id', 'employee_name', 'created_at')
    list_display_links = ('id', 'trade_point_id',)
    search_fields = (
        'trade_point_id__name',
        'trade_point_id__employee_id__full_name',
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def employee_name(self, obj):
        return obj.trade_point_id.employee_id
