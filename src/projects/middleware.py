from django.core.cache import cache
from .models import Project, AnonymousProject

class ProjectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        
        # print(request.session.get('project_handle'))
        if not hasattr(request, "project"):
            request.project = AnonymousProject()
            # print(request.project.is_activated)
            if request.user.is_authenticated:
                project_handle = request.session.get('project_handle')
                project_obj = None
                cache_str = None
                # print(request.project.is_activated)

                if project_handle is not None: 
                    cache_str = f'_project_handle_cache_{project_handle}'
                    project_obj = cache.get(cache_str)

                if project_obj is None and project_handle is not None:
                    try:
                        project_obj = Project.objects.get(handle=project_handle)
                    except:
                        pass
                
                if project_obj is not None:
                    cache.set(cache_str, project_obj)
                    request.project = project_obj
                    # print(request.project.is_activated, project_obj)
        return self.get_response(request)