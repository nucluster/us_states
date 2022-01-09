from django.contrib import admin
from .models import State


@admin.register(State)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('name', 'zip_code', 'capital', 'largest_city',
                    'ratification', 'population', 'total_area', 'land_area',
                    'water_area')
