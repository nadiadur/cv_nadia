from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Profile, Skill
from .forms import ProfileForm, SkillForm
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'frontend/profiles/list.html', {'profiles': profiles})


def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)  # ✅ tambahkan request.FILES
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'frontend/profiles/form.html', {'form': form})


def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)  # ✅ request.FILES juga di sini
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'frontend/profiles/form.html', {'form': form})


def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')
    return render(request, 'frontend/profiles/delete.html', {'profile': profile})

# --- Skill CRUD ---

def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'frontend/skills/list.html', {'skills': skills})

def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'frontend/skills/form.html', {'form': form})

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

def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('skill_list')
    return render(request, 'frontend/skills/delete.html', {'skill': skill})

