from django.shortcuts import render, redirect
from.models import Food
from.forms import Foodf
# Create your views here.
def home(request):
    food=Food.objects.all()
    return render(request,'index.html',{'food':food})
def detail(request,id):
    food=Food.objects.get(id=id)

    return render(request,'detail.html',{'food':food})
def add(request):
    if request.method=='POST':
        name=request.POST['name']
        desc=request.POST['desc']
        price=request.POST['price']
        img=request.FILES['img']
        food=Food(name=name,desc=desc,price=price,img=img)
        food.save()
        return redirect('/')
    return render(request,'add.html')
def update(request,id):
    food=Food.objects.get(id=id)
    form=Foodf(request.POST or None,request.FILES,instance=food)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form})
def delete(request,id):
    food=Food.objects.get(id=id)
    food.delete()
    return redirect('/')