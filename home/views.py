from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,template_name='home/home.html')

def about(request):
    return render(request,template_name='home/about.html')
    
def contact(request):
    return render(request,template_name='home/contact.html')
        
def skill(request):
    return render(request,template_name='home/skill.html')
            
def project(request):
    return render(request,template_name='home/project.html')

