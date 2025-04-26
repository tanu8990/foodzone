from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
     menu=CategoryA.objects.all()
     team=Team.objects.all()
     products={}
     for x in menu:
        products[x]= ProductA.objects.filter(category=x)
     print(products)
     return render(request,'index.html',{'menu':menu, 'products': products,'team':team})


def about(request):
    return render(request,'about.html')

def contact_us(request):
    context={}
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        obj = Contact(name=name,email=email,subject=subject,message=message)
        obj.save()
        context['message']=f"Dear {name}, Thanks for your time!"
    return render(request,'contact.html',context)


def menu(request):
    product=ProductA.objects.all()
    category=CategoryA.objects.all()
    
    
    
    data={'product':product,'category':category}
    return render(request,'menu.html',data)

def getProduct(request, id):
    category=CategoryA.objects.all()
    product = ProductA.objects.filter(category=id)
    if id:
        product = ProductA.objects.filter(category=id)
    else:
        product = ProductA.objects.all()
        
    data={'product':product,'category':category}
    return render(request,'menu.html',data)
    



def booking(request):
    data=0
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        date=request.POST.get('date')
        time=request.POST.get('time')
        person=request.POST.get('person')
        if name !='' and email !='' and number !='' and date !='' and time !='' and person !='':
            data = Table(name=name,email=email,number=number,date=date,time=time,person=person)
            data.save()
    return render(request,'booking.html',{'data':data})

def single(request):
    return render(request,'single.html')