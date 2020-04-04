from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from login_app import views as login_views
from django.conf import settings
from django.conf.urls.static import static
from catalog_app import views as catalog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', catalog_views.index, name="index" ),
    path('register/', login_views.register, name="register"),
    path('profile/', login_views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name="login_app/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="login_app/logout.html"), name='logout'),
    path('delete_account/', login_views.delete_account, name='delete_account'),
    path('mybooks/', catalog_views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('', include('catalog_app.urls')),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)