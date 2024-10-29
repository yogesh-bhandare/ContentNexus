from .models import Project
from . import cache as project_cache

def user_project_context(request):
    username = None
    project_qs = Project.objects.none()
    if request.user.is_authenticated:
        username = request.user.username
        project_qs = project_cache.get_user_projects(username=username)
    return {
        "project_list":project_qs
    }