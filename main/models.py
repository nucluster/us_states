from django.db import models
import django_tables2 as tables


class State(models.Model):
    name = models.CharField('Название штата', max_length=50, unique=True)
    zip_code = models.CharField('Почтовый код', max_length=2, unique=True)
    capital = models.CharField('Столица штата', max_length=50)
    largest_city = models.CharField('Крупнейший город', max_length=50,
                                    blank=True)
    ratification = models.DateField('Дата присоединения')
    population = models.IntegerField('Население')
    total_area = models.DecimalField('Площадь, кв.км', max_digits=10,
                                     decimal_places=2)
    land_area = models.DecimalField('Площадь суши, кв.км', max_digits=10,
                                    decimal_places=2)
    water_area = models.DecimalField('Площадь воды, кв.км', max_digits=10,
                                     decimal_places=2)
    flag_image = models.ImageField('Флаг', null=True, blank=True)
    seal_image = models.ImageField('Печать', null=True, blank=True)

    def __str__(self):
        return self.name


class StateTable(tables.Table):
    class Meta:
        model = State
        attrs = {"class":"table table-striped table-bordered"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'name', 'zip_code', 'capital', 'largest_city',
                    'ratification', 'population', 'total_area', 'land_area',
                    'water_area')

