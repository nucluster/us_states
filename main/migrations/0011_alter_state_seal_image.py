# Generated by Django 3.2.11 on 2022-01-19 19:11

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20220116_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='seal_image',
            field=models.FileField(blank=True, null=True, upload_to=main.models.seal_directory_path, verbose_name='Печать'),
        ),
    ]
