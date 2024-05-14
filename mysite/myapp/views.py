from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Profile
from django.http import JsonResponse
def welcome(request):
    return render(request,'index.html')

def ProfileView(request):
    if request.method=="POST":
        name = request.POST.get("name","")
        mobile_number= request.POST.get("mobile_number","")
        address = request.POST.get("address", "")
        email = request.POST.get("email", "")
        if name and email:
            Profile.objects.create(name=name, address=address, mobile_number=mobile_number, email=email)
        else:
            return render(request, 'profile.html', {"error_message": "Name and Email are required fields"})
        return redirect('profile')
    else:
        stored_profiles = Profile.objects.all()
        context = {'stored_profiles': stored_profiles}
        return render(request, 'profile.html', context)
    
def get_profile_by_name(request, name):
    try:
        profile = Profile.objects.get(name=name)
        user_data = {
            "name" : profile.name,
            "address" : profile.address,
            "mobile_number" : profile.mobile_number,
            "email" : profile.email,
        }
        return JsonResponse(user_data)
    except Profile.DoesNotExist as e:
        error_message = f"Profile '{name}' does not exist: {str(e)}"
        error_data = {"error" : error_message}
        return JsonResponse(error_data, status = 404)
    
