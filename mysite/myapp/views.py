from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Profile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
import json
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




  
def update_email(request,name):
    if request.method=='PUT':
        try:
            profile=Profile.objects.get(name=name)
            data=json.loads(request.body)
            new_email=data.get("email")
            
            try:
                validate_email(new_email)
            except ValidationError as e:
                return JsonResponse({"error": str(e)}, status=400)
            if new_email:
                profile.email=new_email
                profile.save()
                return JsonResponse({"message" : "Email updated successfully"})
            else:
                return JsonResponse({"error": "Email not provided in request body"}, status=400)

        except Profile.DoesNotExist as e:
            error_message = f"Profile '{name}' does not exist: {str(e)}"
            error_data = {"error" : error_message}
            return JsonResponse(error_data, status = 404)
    else:
        return JsonResponse({"error" : "only 'PUT' request are allowed"}, status = 404)

def update_name(request,name):
    if request.method=='PUT':
        try:
            profile=Profile.objects.get(name=name)
            data=json.loads(request.body)
            new_name=data.get("name")
            if new_name:
                profile.name=new_name
                profile.save()
                return JsonResponse({"message" : "Name updated successfully"})
            else:
                return JsonResponse({"error": "Name not provided in request body"}, status=400)

        except Profile.DoesNotExist as e:
            error_message = f"Profile '{name}' does not exist: {str(e)}"
            error_data = {"error" : error_message}
            return JsonResponse(error_data, status = 404)
    else:
        return JsonResponse({"error" : "only 'PUT' request are allowed"}, status = 404)

def Delete_Profile(request,name):
    if request.method=='POST':
       Delete_User= Profile.objects.get(name=name) 
       Delete_User.delete()
       return JsonResponse({"message":"Profile Deleted Successfully"})
    else:
        return JsonResponse({"error" : "only 'POST' request are allowed"}, status = 404)