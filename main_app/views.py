from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from .models import Candy, Store
# from .forms import CandyForm, StoreForm


# ------------------- STATIC
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# ------------------- CANDY
def candy_index(request):
    all_candy = Candy.objects.all()
    context = {
        'all_candy': all_candy
    }
    return render(request, 'candy/index.html', context)


def candy_detail(request, candy_id):
    candy = Candy.objects.get(id=candy_id)
    context = {
        'candy': candy
    }
    return render(request, 'candy/detail.html', context)




# ------------------- STORES
@login_required
def user_stores(request):
    # stores = Store.objects.filter(user=request.user)
    # context = {
    #     'stores': stores
    # }
    return render(request, 'stores/user_index.html')


# ------------------- PROFILE/USER
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_stores')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)

