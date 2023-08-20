from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news_home, name='news'),            # Основная страница новостей
    path('<int:pk>', views.NewsDetailView.as_view(), name='NewsDetail')  # Детали новости по ее pk (id)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
