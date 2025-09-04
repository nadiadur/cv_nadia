from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from rest_framework import viewsets
from .models import Profile
from .forms import ProfileForm
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'frontend/profiles/list.html', {'profiles': profiles})

def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'frontend/profiles/form.html', {'form': form})

def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
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
