from django import forms
from .models import Profile, Skill, OrganizationExperience

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'address', 'phone', 'email', 'github', 'summary', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['profile', 'name', 'category']
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
        }

class OrganizationExperienceForm(forms.ModelForm):
    class Meta:
        model = OrganizationExperience
        fields = ['profile', 'role', 'organization', 'period', 'description']
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'organization': forms.TextInput(attrs={'class': 'form-control'}),
            'period': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }