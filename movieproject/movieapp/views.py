from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movie_form
from .models import movie

# Create your views here.
def index(request):
    m=movie.objects.all()
    c={
        'list':m
    }
    return render(request,'index.html',c)
def detail(request,movie_id):
    mov=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'m':mov})

def add_movie(request):
    if request.method == "POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img=request.FILES['img']
        mov=movie(name=name,desc=desc,year=year,img=img)
        mov.save()
    return render(request,'add.html')
def update(request,id):
    mov=movie.objects.get(id=id)
    form=movie_form(request.POST or None,request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'mov':mov})
def delete(request,id):
    if request.method == 'POST':
        mov=movie.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request,'delete.html')




