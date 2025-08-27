from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    github = models.CharField(max_length=100, blank=True, null=True)
    summary = models.TextField()
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  

    def __str__(self):
        return self.name

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200, blank=True, null=True)
    semester = models.CharField(max_length=50, blank=True, null=True)
    image1 = models.ImageField(upload_to='project_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='project_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='project_images/', blank=True, null=True)
    def __str__(self):
        return self.title
class OrganizationExperience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='organizations')
    role = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    period = models.CharField(max_length=50)
    description = models.TextField()
