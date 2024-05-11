from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Profile
def welcome(request):
    return render(request,'index.html')

def ProfileView(request):
    if request.method=="POST":
        name = request.POST.get("name","")
        Profile.object.create(name=name)
        return redirect('Profile')
    
    else:
        stored_names=Profile.objects.all()
        context={'stored_names':stored_names}
        return render('request',profile.html,context)