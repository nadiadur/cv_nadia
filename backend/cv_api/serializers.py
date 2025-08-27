from rest_framework import serializers
from .models import Profile, Education, Skill, Project, OrganizationExperience

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class OrganizationExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationExperience
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    organizations = OrganizationExperienceSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
