from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Candy, Store
from .forms import CandyForm, StoreForm


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


@login_required
def add_candy(request, store_id):
    store = Store.objects.get(id=store_id)
    candy_form = CandyForm()
    context = {
            'candy_form': candy_form,
            'store': store
        }
    if request.method == 'POST':
        print(candy_form)
        print(request.user)
        candy_form = CandyForm(request.POST)
        candy_form.seller = request.user
        if candy_form.is_valid():
            candy_form.save(commit=False)
            candy_form.seller = request.user
            candy_form.save()
            return redirect('store_detail', context)
    else:
        return render(request, 'candy/new.html', context)




# ------------------- STORES
@login_required
def user_stores(request):
    stores = Store.objects.filter(user=request.user)
    context = {
        'stores': stores
    }
    return render(request, 'stores/user_index.html', context)


def stores_index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores
    }
    return render(request, 'stores/index.html', context)


def store_detail(request, store_id):
    store = Store.objects.get(id=store_id)
    all_candy = Candy.objects.filter(seller=store.id)

    context = {
        'store': store,
        'all_candy': all_candy,
    }
    return render(request, 'stores/detail.html', context)



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

