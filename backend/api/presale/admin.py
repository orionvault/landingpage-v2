from django.contrib import admin
from .models import PresaleOrder


class AdminPresale(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contribution', 'currency', 'created_at')
    list_filter = ('currency', 'investor_type')
    search_fields = ['first_name', 'last_name', 'email']

admin.site.register(PresaleOrder, AdminPresale)
