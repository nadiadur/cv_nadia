from django import forms
from .models import Profile, Skill, OrganizationExperience, Education, Project

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

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['profile', 'start_year', 'end_year', 'degree', 'institution', 'gpa']
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-control'}),
            'start_year': forms.TextInput(attrs={'class': 'form-control'}),
            'end_year': forms.TextInput(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['profile', 'title', 'description', 'tech_stack', 'semester', 'image1', 'image2', 'image3']
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':4}),
            'tech_stack': forms.TextInput(attrs={'class': 'form-control'}),
            'semester': forms.TextInput(attrs={'class': 'form-control'}),
            'image1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'image2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'image3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }