from django.shortcuts import render, get_object_or_404
from cv_api.models import Project

# Create your views here.
def home(request):
    return render(request, 'home.html')

def project_detail(request):
    project_id = request.GET.get('id')
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'single-portfolio.html', {'project': project})
