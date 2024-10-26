from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('', include('home.urls')), # define a rota para a página inicial
    path('projetos/', include('projetos.urls')),
    path('tarefas/', include('tarefas.urls')),
    ]