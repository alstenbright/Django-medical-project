from django.shortcuts import render
from .models import Customer
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home(request):
    return render(request, 'index.html', context={})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                if Customer.objects.filter(username=username).exists():
                    error_message = "Username is already taken."
                    return render(request, 'signup.html', {'form': form, 'error_message': error_message})
                else:
                    user = User(username=username, password=password)
                    user.set_password(password)
                    user.save()
                    return redirect('login') 
            else:
                error_message = "Passwords do not match."
                return render(request, 'signup.html', {'form': form, 'error_message': error_message})
    else:
        form = SignupForm()
    return render(request, 'signup.html',{'form':form})

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login 

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('create')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }
    return render(request, 'logout.html', context)










