from django.contrib import admin

from .models import Broker


class BrokerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Broker, BrokerAdmin)
