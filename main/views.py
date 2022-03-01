from django.http import HttpResponse, HttpResponseRedirect
import django_tables2 as tables
from django.shortcuts import render

from .models import State
from .tables import StateTable
from .forms import UploadFileForm
from .generate_key import gen_random_key
from us_states.settings import BASE_DIR


class TableView(tables.SingleTableView):
    table_class = StateTable
    queryset = State.objects.all()
    template_name = "main/hello.html"
    table_pagination = False
    ordering = ('id',)


# key = gen_random_key(2,3,5)

def get_key(request):
    return HttpResponse(gen_random_key(2,3,5))


def handle_uploaded_file(f):
    with open('screenshot.png', 'wb+') as destination:
        destination.write(f)
        # for chunk in f.chunks():
        #     destination.write(chunk)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('')
    else:
        form = UploadFileForm()
    return render(request, 'main/upload.html', {'form': form})
