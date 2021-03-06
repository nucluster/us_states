import django_tables2 as tables
from django.utils.html import format_html
from .models import State


class ImageColumnFlag(tables.Column):
    def render(self, value):
        return format_html(
            '<a href="/media/{0}"><img src="/media/{0}.png" width="100" '
            'height="66" alt="{0}"/>', value)


class ImageColumnSeal(tables.Column):
    def render(self, value):
        return format_html(
            '<a href="/media/{0}"><img src="/media/{0}.png" width="50" '
            'height="50" alt="{0}" />', value)


class StateTable(tables.Table):
    id = tables.Column(verbose_name='#',
                       attrs={"th": {"style": "font-size: 32px"},
                              "td": {"style": "font-weight: bold"}}
                       )
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
