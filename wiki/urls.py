from django.urls import path
from wiki.views import PageListView, PageDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
