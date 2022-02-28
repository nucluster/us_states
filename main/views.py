from django.http import HttpResponse
import django_tables2 as tables
from .models import State
from .tables import StateTable


class TableView(tables.SingleTableView):
    table_class = StateTable
    queryset = State.objects.all()
    template_name = "main/hello.html"
    table_pagination = False
    ordering = ('id',)


key = 'W8H74-7F63C-Y44W4-379XJ-23FMF'


def get_key(request):
    return HttpResponse(key)
