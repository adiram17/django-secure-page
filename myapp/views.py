from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def unsecure(request):   
    return render(request,"unsecure.html",{})  

@login_required
def secure(request):   
    return render(request,"secure.html",{})  
