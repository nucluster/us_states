# Generated by Django 3.2.11 on 2022-01-09 13:09

from django.db import migrations


def csv_to_db(apps, schema_editor):
    State = apps.get_model('main', 'State')

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_state_largest_city'),
    ]

    operations = [
    ]
