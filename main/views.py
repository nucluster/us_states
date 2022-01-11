from django.shortcuts import render
import django_tables2 as tables
from .models import State, StateTable


# def hello(request):
#     return render(request, 'main/hello.html', {})


class TableView(tables.SingleTableView):
    table_class = StateTable
    queryset = State.objects.all()
    template_name = "main/hello.html"
    table_pagination = False

# tables.SingleTableView.table_pagination = False