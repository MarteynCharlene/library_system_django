from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'catalog_app'

urlpatterns = [
    path('', views.index, name='index2'),
    path('borrowing_a_book', views.borrowing_a_book, name='borrowing_a_book'),  
    path('borrowing_a_magazine', views.borrowing_a_magazine, name='borrowing_a_magazine'),
    path('return_book', views.return_book, name='return_book'),
    path('return_magazine', views.return_magazine, name='return_magazine'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)