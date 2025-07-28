from django.urls import path, include
from django.contrib import admin  # Correção aqui
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    # path('api/', include('your_api_app.urls')),  # Comente ou ajuste para o nome real do app
]