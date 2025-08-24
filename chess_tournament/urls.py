from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login'), name='home'),  # redirect root to login
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', include('tournament.auth_urls')),
    path('tournament/', include('tournament.urls')),  # move tournament under its own path
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)