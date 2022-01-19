# Generated by Django 3.2.11 on 2022-01-19 19:12

from django.db import migrations
from main.models import flag_directory_path, seal_directory_path 


def fill_flags_seals_(apps, schema_editor):
    State = apps.get_model('main', 'State')
    # State.objects.update_or_create(flag_image=flag_directory_path(obj,filename=False),
    #                                 seal_image=seal_directory_path)
    for state in State.objects.all():
        state.flag_image=flag_directory_path(state, filename=False)
        state.seal_image=seal_directory_path(state, filename=False)
        state.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_state_seal_image'),
    ]

    operations = [
        migrations.RunPython(fill_flags_seals_),
    ]
