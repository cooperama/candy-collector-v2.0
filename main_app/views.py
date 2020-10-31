from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from .models import Candy, Store
# from .forms import CandyForm, StoreForm


# ------------------- STATIC
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')
