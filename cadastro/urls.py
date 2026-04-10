# cadastro\urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Rota da página inicial
    path('', views.index, name='index'),

    # Rota da página 'Contatos'
    path('contato/', views.contato, name='contato'),

    # Rota para cadastrar pessoa
    path('adicionar/', views.adicionar, name='adicionar'),
]