# Generated by Django 3.2.11 on 2022-01-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_state_ratification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='land_area',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Площадь суши, кв.км'),
        ),
    ]