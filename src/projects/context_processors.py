from django.core.cache import cache
from .models import Project

def user_project_context(request):
    project_qs = Project.objects.none()
    if request.user.is_authenticated:
        cache_str = f'_user_project_cache_{request.user.username}'
        project_qs = cache.get(cache_str)
        if project_qs is None:
            project_qs = Project.objects.filter(owner=request.user)
            cache.set(cache_str, project_qs)
    return {
        "project_list":project_qs
    }