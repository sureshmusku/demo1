from django.shortcuts import render,redirect
from django .http import  HttpRequest, HttpResponse

# Create your views here.
from.models import Student
from.forms import StudentForm



def index (request):
    obj=Student.objects.all()
    context={'stdobj':obj

             }
    return render (request,"javaapp/display.html",context)


def add_book(request):
    if request.method == "POST":
        name=request.POST.get('name')
        marks=request.POST.get('marks')
        obj=Student(name=name,marks=marks)
        obj.save()
        return redirect('/')
    return render(request,'javaapp/add_book.html')



def update(request,id):
    obj=Student.objects.get(id=id)
    form=StudentForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'javaapp/edit.html',{'form':form,'student':obj})

def delete(request,id):
    obj=Student.objects.get(id=id)
    obj.delete()
    obj.save()
    return redirect('/')
    return render(request,'javaapp/display.html')

















