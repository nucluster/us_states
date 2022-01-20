from django.db import models


def flag_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/zip_code/<filename>
    filename = 'Flag_of_{}.svg'.format(instance.name.replace(' ', '_'))
    return '{0}/{1}'.format(instance.zip_code, filename)


def seal_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/zip_code/<filename>
    filename = 'Seal_of_{}.svg'.format(instance.name.replace(' ', '_'))
    return '{0}/{1}'.format(instance.zip_code, filename)


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
    flag_image = models.FileField('Флаг', null=True, blank=True,
                                    upload_to=flag_directory_path)
    seal_image = models.FileField('Печать', null=True, blank=True,
                                    upload_to=seal_directory_path)

    def __str__(self):
        return self.name
