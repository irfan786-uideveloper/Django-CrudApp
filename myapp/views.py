from django.shortcuts import render,redirect

from .models import Student

from .forms import Studentform

# Create your views here.

def Home(request):
    student=Student.objects.all
    form=Studentform
    return render(request,'Home.html',{'form':form,'student':student})

def add(request):
    form=Studentform(request.POST)
    form.save()
    return redirect('/')

def Edit(request,id):
    student=Student.objects.get(id=id)
    return render(request,'Edit.html',{'student':student})

def update(request,id):
    student=Student.objects.get(id=id)
    form=Studentform(request.POST,instance=student)
    form.save()
    return redirect('/')


def delete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/')