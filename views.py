from django.shortcuts import render, redirect
from index.models import Contact

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        concern = request.POST['concern']
        print(name, email, phone, concern)
        
        # Save the contact information to the database
        obj = Contact(name=name, email=email, phone=phone, concern=concern)
        obj.save()
        
        # Optionally, redirect to a success page or give feedback
        return redirect('home')  # Redirecting to home after successful submission
    
    return render(request, 'contact.html')