from django.shortcuts import redirect, render
from .models import customer
#from django.contrib import messages
#from django.contrib.auth import authenticate,login,logout
#from django.views.decorators.cache.import never_cache
#from django.db.models import Q




# Create your views here.
def crud(request):
   cus = customer.objects.all()

   context = {
      'cus':cus,
   }
   return render(request,'crud.html',context)
   """ stu=None
    if request.method=='POST':
        fm=Aforms(request.POST)
        
        if fm.is_valid():
            fm.save()

        fm=Aforms()
        stu=Amodel.objects.all()
        print(stu,"||||||||||||||||||||")

    else:
        fm=Aforms()

    return render(request,'add.html',{'fm':fm,'stu':stu})
"""
def add(request):
   if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')

        cus=customer(
            name = name,
            email =email
        )
        cus.save()
        return redirect('crud')
   return render(request,'crud.html')
"""
def edit(request):
    cus=customer.objects.all()

    context = {
        'cus':cus,
    }
    return redirect(request,'crud.html',context)
    
"""

def update(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']

        cus = customer.objects.get(id=id)
        cus.name = name
        cus.email = email
        cus.save()
        return redirect('crud')
    


def delete(request,id):
    cus=customer.objects.filter(id=int(id))
    cus.delete()
    return redirect('crud')