from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .form import Form
# Create your views here.

def home(request):
    obj= Product.objects.all()
    context= {
        'data': obj
    }
    return render(request, 'data.html', context)

def create(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = Form()
    context = {
            'form':form,
        }
    return render(request, 'input.html', context)

# def edit(request, id):
#     obj= Product.objects.get(id= id)
#     context= {
#         'data': obj
#     }
#     return render(request, 'edit.html', context)

def update(request, id):
    obj= Product.objects.get(id= id)
    if request.method== "POST":
        
        print(obj)
        form1 = Form(request.POST, instance= obj)
        if form1.is_valid():
            print(("++++++++++++"))
            form1.save()
            return redirect('home')
    form = Form()
    context = {
            'form':form,
        }   
    return render(request, 'edit.html',context )


def del_product(request, id):
   
    if request.method== "POST":
        obj= Product.objects.get(id= id).delete()
        return redirect('home')
    return render(request, 'delete.html')    