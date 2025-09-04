import requests
from django.shortcuts import render, get_object_or_404, redirect
from cv_api.models import Project, Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout
from cv_api.forms import ProfileForm



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



def profile_list(request):
    profiles = Profile.objects.all()  
    return render(request, 'frontend/pages-profile.html', {'profiles': profiles})






@login_required(login_url="login")
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, "frontend/profiles/list.html", {"profiles": profiles})


@login_required(login_url="login")
def profile_create(request):
    if request.method == "POST":
        Profile.objects.create(
            name=request.POST.get("name"),
            address=request.POST.get("address"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            github=request.POST.get("github"),
            summary=request.POST.get("summary"),
            image=request.FILES.get("image"), 
        )
        return redirect("profile_list")
    return render(request, "frontend/profiles/form.html")


@login_required(login_url="login")
def profile_update(request, id):
    profile = get_object_or_404(Profile, id=id)
    if request.method == "POST":
        profile.name = request.POST.get("name")
        profile.address = request.POST.get("address")
        profile.phone = request.POST.get("phone")
        profile.email = request.POST.get("email")
        profile.github = request.POST.get("github")
        profile.summary = request.POST.get("summary")
        if request.FILES.get("image"):
            profile.image = request.FILES.get("image")
        profile.save()
        return redirect("profile_list")
    return render(request, "frontend/profiles/form.html", {"profile": profile})


@login_required(login_url="login")
def profile_delete(request, id):
    profile = get_object_or_404(Profile, id=id)
    if request.method == "POST":
        profile.delete()
        return redirect("profile_list")
    return render(request, "frontend/profiles/delete.html", {"profile": profile})

def profile_add(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile-list')
    else:
        form = ProfileForm()
    return render(request, 'frontend/profile_add.html', {'form': form})

def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'frontend/profile_edit.html', {'form': form, 'profile': profile})