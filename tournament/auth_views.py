from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import AdminProfile

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            AdminProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Welcome! Your account has been created successfully.')
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    
    return render(request, 'auth/register.html', {'form': form})