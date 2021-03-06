
# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic 
from .models import CustomUser 
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required



class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'



class UserProfile(generic.ListView):
    template_name = 'users/profile.html'
    model = CustomUser
    context_object_name = 'profile'

    
