from django.shortcuts import render
from .models import Artiles
from django.views.generic import DetailView
from django.core.paginator import Paginator

def news_home(request):
    articles_list = Artiles.objects.all().order_by('-date')  # Отсортировать статьи по дате
    paginator = Paginator(articles_list, 3)  # Показать 4 статьи на одной странице

    page = request.GET.get('page')  # Получить номер страницы из запроса
    articles = paginator.get_page(page)

    return render(request, 'news/news_home.html', {'articles': articles})

class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'artiles'



