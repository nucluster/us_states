# Generated by Django 3.2.11 on 2022-01-16 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_fill_largest_city_20220111_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='flag_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Флаг'),
        ),
        migrations.AlterField(
            model_name='state',
            name='seal_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Печать'),
        ),
    ]