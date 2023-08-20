from django.shortcuts import render
from .models import File, ArtLine, Home
from django.views.generic import DetailView
from django.core.paginator import Paginator

def layout(request):
    con_home = Home.objects.all()
    return render(request, 'main/layout.html', {'con_home':con_home})

def index(request):
    files_list = File.objects.all().order_by('-uploaded_at')
    paginator = Paginator(files_list, 3)

    page = request.GET.get('page')
    files = paginator.get_page(page)

    return render(request, 'main/index.html', {'files': files})

def about(request):
    con_data = ArtLine.objects.all()
    return render(request, 'main/about.html', {'con_data': con_data})


