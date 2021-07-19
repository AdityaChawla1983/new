from os import stat
from django.shortcuts import redirect
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import (
ArticleListView,
ArticleUpdateView,
ArticleDetailView,
ArticleDeleteView, 
ArticleCreateView
)
from .views import redirect_view
urlpatterns = [
path('<int:pk>/edit/',
ArticleUpdateView.as_view(), name='article_edit'), # new
path('<int:pk>/',
ArticleDetailView.as_view(), name='article_detail'), # new
path('<int:pk>/delete/',
ArticleDeleteView.as_view(), name='article_delete'), # new
path('new/', ArticleCreateView.as_view(), name='article_new'),
path('', ArticleListView.as_view(), name='article_list'),
path('article_list', redirect_view)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
