from django.shortcuts import render
import django_tables2 as tables
from .models import State, StateTable


class TableView(tables.SingleTableView):
    table_class = StateTable
    queryset = State.objects.all()
    template_name = "main/hello.html"
    table_pagination = False
    ordering = ('id',)
