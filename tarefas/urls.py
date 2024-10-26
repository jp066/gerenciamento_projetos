from django.urls import path
from . import views

urlpatterns = [
    path('criar-tarefa/', views.tarefa_create, name='create_tarefa'),
    path('tarefa/<int:id>/', views.tarefa_detalhe, name='tarefa_detalhe'),
    path('tarefa/<int:id>/delete/', views.tarefa_delete, name='tarefa_delete'),
    path('tarefa/<int:id>/update/', views.tarefa_update, name='tarefa_update'),
    ]