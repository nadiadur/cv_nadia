import requests
from django.shortcuts import render, get_object_or_404, redirect
from cv_api.models import Project, Profile, Skill, OrganizationExperience, Education, Project
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout
from cv_api.forms import ProfileForm, SkillForm, OrganizationExperienceForm, EducationForm, ProjectForm


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

# ================= PROFILE CRUD =================

@login_required(login_url="login")
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, "frontend/profiles/list.html", {"profiles": profiles})

@login_required(login_url="login")
def profile_add(request): 
    if request.method == "POST":
        print("=== DEBUG ADD PROFILE ===")
        print("POST data:", request.POST)
        print("FILES data:", request.FILES)
        print("Has image:", 'image' in request.FILES)
        
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save()
            print(f"Profile saved: {profile.name}")
            print(f"Image saved: {profile.image}")
            return redirect('profile-list')
        else:
            print("Form errors:", form.errors)
    else:
        form = ProfileForm()
    return render(request, 'frontend/profiles/form.html', {'form': form})

@login_required(login_url="login")
def profile_edit(request, pk): 
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        print("=== DEBUG EDIT PROFILE ===")
        print("POST data:", request.POST)
        print("FILES data:", request.FILES)
        print("Current image:", profile.image)
        
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            updated_profile = form.save()
            print(f"Profile updated: {updated_profile.name}")
            print(f"New image: {updated_profile.image}")
            return redirect('profile-list')
        else:
            print("Form errors:", form.errors)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'frontend/profiles/form.html', {'form': form, 'profile': profile})

@login_required(login_url="login")
def profile_delete(request, pk): 
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        profile.delete()
        return redirect('profile-list')
    return render(request, "frontend/profiles/delete.html", {"profile": profile})

@login_required(login_url="login")
def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'frontend/skills/list.html', {'skills': skills})

@login_required(login_url="login")
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'frontend/skills/form.html', {'form': form})

@login_required(login_url="login")
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'frontend/skills/form.html', {'form': form})

@login_required(login_url="login")
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('skill_list')
    return render(request, 'frontend/skills/delete.html', {'skill': skill})
def org_list(request):
    orgs = OrganizationExperience.objects.all()
    return render(request, 'frontend/orgs/list.html', {'orgs': orgs})

def org_create(request):
    if request.method == 'POST':
        form = OrganizationExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('org_list')
    else:
        form = OrganizationExperienceForm()
    return render(request, 'frontend/orgs/form.html', {'form': form})

def org_edit(request, pk):
    org = get_object_or_404(OrganizationExperience, pk=pk)
    if request.method == 'POST':
        form = OrganizationExperienceForm(request.POST, instance=org)
        if form.is_valid():
            form.save()
            return redirect('org_list')
    else:
        form = OrganizationExperienceForm(instance=org)
    return render(request, 'frontend/orgs/form.html', {'form': form})

def org_delete(request, pk):
    org = get_object_or_404(OrganizationExperience, pk=pk)
    if request.method == 'POST':
        org.delete()
        return redirect('org_list')
    return render(request, 'frontend/orgs/delete.html', {'org': org})

@login_required(login_url="login")
def edu_list(request):
    educations = Education.objects.all()
    return render(request, 'frontend/education/list.html', {'educations': educations})

@login_required(login_url="login")
def edu_create(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu_list')
    else:
        form = EducationForm()
    return render(request, 'frontend/education/form.html', {'form': form})

@login_required(login_url="login")
def edu_edit(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('edu_list')
    else:
        form = EducationForm(instance=education)
    return render(request, 'frontend/education/form.html', {'form': form})

@login_required(login_url="login")
def edu_delete(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        education.delete()
        return redirect('edu_list')
    return render(request, 'frontend/education/delete.html', {'education': education})

@login_required(login_url="login")
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'frontend/projects/list.html', {'projects': projects})

@login_required(login_url="login")
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'frontend/projects/form.html', {'form': form})

@login_required(login_url="login")
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'frontend/projects/form.html', {'form': form})

@login_required(login_url="login")
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'frontend/projects/delete.html', {'project': project})


def dashboard(request):
    context = {
        'profile_count': Profile.objects.count(),
        'education_count': Education.objects.count(),
        'skill_count': Skill.objects.count(),
        'project_count': Project.objects.count(),
        'org_count': OrganizationExperience.objects.count(),
    }
    return render(request, 'frontend/dashboard.html', context)




def homepage(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, 'home.html', {'profile': profile})
