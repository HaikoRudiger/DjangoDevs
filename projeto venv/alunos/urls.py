from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='index'),
    path ('aluno', views.aluno, name='aluno')
=======
    path('', views.index, name='index'), 
    path('aluno', views.aluno, name='aluno'),
>>>>>>> d8ff73cdfbbf6c7dbfb8eb509b680c0e94d4eaaf
]