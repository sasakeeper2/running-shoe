from django.shortcuts import render
from .models import RunningShoe
from .forms import ShoeSearchForm
from django.contrib.auth import login
from .forms import SignupForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def recommend_shoes(request):
    form = ShoeSearchForm(request.GET or None)
    results = []

    if form.is_valid():
        data = form.cleaned_data
        results = RunningShoe.objects.filter(
            surface=data['surface'],
            foot_strike=data['foot_strike'],
            cushioning=data['cushioning'],
            pronation_support=data['pronation_support']
        )

    return render(request, 'shoes/recommend.html', {'form': form, 'results': results})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recommend_shoes')  # Redirect to the recommendation page after login
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password!
            user.save()
            login(request, user)
            return redirect('recommend_shoes')  # Redirect to the recommendation page after signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

