from django.shortcuts import render
from django.http import JsonResponse
# Ensure your model names match the capitalization in your models.py
from .models import Contact, Skill, Project, Experience, Profile

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        if name and email and message:
            # Capitalized Contact to match standard class naming
            Contact.objects.create(name=name, email=email, message=message)
            
            return JsonResponse({
                "status": "success",
                "message": f"Thank you for your message {name}. We will get back to you soon."          
            })
            
        else:
            return JsonResponse({
                "status": "error",
                "message": "Please fill out all fields."
            })
            
    # Fetch all database records
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    profile = Profile.objects.first()
    
    # Pass them to the template
    context = {
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'profile': profile
    }
    
    return render(request, 'index.html', context)