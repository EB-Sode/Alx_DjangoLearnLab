from django.shortcuts import render, redirect
from .models import Post
from .forms import CustomUserCreationForm, ProfileEditForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

# Create your views here.

class RegisterView(View):
    '''get form from forms.py'''
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request,'blog/register.html', {'form':form} )
    '''save form to database'''
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base')
        return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated")
            return redirect('profile')
    else:
        form = ProfileEditForm(instance = request.user)
    return render(request, 'blog/profile.html', {'form': form})

# Login & Logout (using Django's built-in views)
class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'