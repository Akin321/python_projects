from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def operation(request):
    x=int(request.GET['n1'])
    y=int(request.GET['n2'])
    a=x+y
    s=x-y
    m=x*y
    d=x/y
    return render(request,'result.html',{'add':a,
                                         'mul':m,'sub':s,'div':d})