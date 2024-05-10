from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm


# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')

# signup page
# def user_signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home URL pattern
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def us