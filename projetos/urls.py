from django.urls import path
from . import views

urlpatterns = [
    path('criar-projetos/', views.projeto_create, name='create_projeto'),
    path('projeto/<int:id>/', views.projeto_detalhe, name='projeto_detalhe'),
    path('projeto/<int:id>/delete/', views.projeto_delete, name='projeto_delete'),
    path('projeto/<int:id>/update/', views.projeto_update, name='projeto_update'),
]