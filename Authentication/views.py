from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from . import forms

# Create your views here.
def register(request):
    if request.method == 'POST':
        pass
    else:
        form = forms.RegisterForm()
    return render(request, 'Authentication/register.html', {'form': form})