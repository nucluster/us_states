from django.shortcuts import render
from .models import State


def get_table(request):
    states = State.objects.all()
    table_headers = [f.verbose_name for f in State._meta.get_fields()]
    context = {'states': states, 'table_headers': table_headers[:-2]}
    return render(request, 'main/hello_bootstrap_table.html', context)