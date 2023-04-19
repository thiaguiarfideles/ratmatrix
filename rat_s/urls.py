from django.urls import path
from . import views
from .views import generate_pdf

app_name = 'rat_s'


urlpatterns = [
    path('', views.cadastrar_prestador_view, name='rat_s'),
    path('gerar_pdf/', views.generate_pdf, name='generate_pdf'),

]