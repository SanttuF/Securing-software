from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PhoneNumber
from django.contrib.auth.password_validation import validate_password

def index(request, search=''):
    try:
        entries = PhoneNumber.objects.filter(name__icontains=search)
    except:
        entries = []
    return render(request, 'phonebook/index.html', {"entries": entries, 'user': request.user.username})

@login_required
def deleteView(request, id):
    if request.method == 'POST':
        entry = get_object_or_404(PhoneNumber, id=id)
        
        print(request.user.username)
        # Flaw 2: To fix, uncomment the two lines below
        if request.user.username != entry.creator:
            return redirect('/')
        
        entry.delete()
    return redirect('/')

# Flaw 1: To fix, uncomment the line below
@login_required
def addView(request):
    if request.method == 'POST':
        creator = request.user.username
        name = request.POST.get('name')
        number = request.POST.get('number')

        PhoneNumber.objects.create(creator=creator, name=name, number=number)
    return redirect('/')

def signupView(request):
    return render(request, 'phonebook/signup.html')
    
    
def createuserView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.create_user(username=username, password=password)
            validate_password(password)
        except Exception as e:
            return render(request, 'phonebook/signup.html', {'error': e})
    return redirect('/')

def userView(request):
    users = User.objects.all()
    return render(request, 'phonebook/users.html', {'users': users})