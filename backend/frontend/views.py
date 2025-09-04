import requests
from django.shortcuts import render, get_object_or_404, redirect
from cv_api.models import Project
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout


def home(request):
    return render(request, 'home.html')

def project_detail(request, id): 
    project = get_object_or_404(Project, id=id)
    return render(request, 'single-portfolio.html', {'project': project})
@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard") 
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "frontend/login.html", {"error": "Username atau password salah"})
    return render(request, "frontend/login.html")


@never_cache
@login_required(login_url="login")
def dashboard(request):
    api_url = "http://127.0.0.1:8000/api/profiles/"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            profiles = response.json()
        else:
            profiles = []
    except:
        profiles = []

    return render(request, "frontend/dashboard.html", {"profiles": profiles})


@never_cache
@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("login")
