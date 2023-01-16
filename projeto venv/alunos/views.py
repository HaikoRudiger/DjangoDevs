from django.shortcuts import render

def index(request):
    return render(request,'index.html', {'nome_do_aluno':'Lirinha'})

def aluno(request):
    return render(request,'aluno.html')


# Create your views here.
