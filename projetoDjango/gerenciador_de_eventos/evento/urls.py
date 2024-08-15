from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_eventos, name='lista_de_evento'),
    path('<int:evento_id>/', views.detalhes_evento, name='detalhe_do_evento'),
]
