from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'catalog_app'

urlpatterns = [
    path('', views.index, name='index2'),
    path('borrowing_a_book', views.borrowing_a_book, name='borrowing_a_book'),  
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)