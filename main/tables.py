import django_tables2 as tables
from django.utils.html import format_html
from .models import State


class ImageColumnFlag(tables.Column):
    def render(self, value):
        return format_html(
            '<a href="/media/{0}"><img src="/media/{0}" width="100" '
            'height="66" />', value)


class ImageColumnSeal(tables.Column):
    def render(self, value):
        return format_html(
            '<a href="/media/{0}"><img src="/media/{0}" width="50" '
            'height="50" />', value)


class StateTable(tables.Table):
    flag_image = ImageColumnFlag()
    seal_image = ImageColumnSeal()

    def render_ratification(self, value):
        return value

    class Meta:
        model = State
        attrs = {"class": "table table-striped table-bordered"}
        fields = ('id', 'name', 'zip_code', 'capital', 'largest_city',
                  'ratification', 'population', 'total_area', 'land_area',
                  'water_area', 'flag_image', 'seal_image')
