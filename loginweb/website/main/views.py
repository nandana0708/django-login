from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "There was an error Logging In. Please Try Again.")
            return redirect('home')
    else:
        return render(request, 'main/home.html', {'records': records})

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #login user 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Your registration Is Successful')
            return redirect('home')
        
    else:
        form = SignUpForm()
        return render(request, 'main/register.html', {'form': form})
    
    return render(request, 'main/register.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')