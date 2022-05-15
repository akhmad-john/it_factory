from django.contrib import admin

from .models import TradePoint


@admin.register(TradePoint)
class TradePointAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'employee_id')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
