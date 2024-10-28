from django.urls import reverse

def site_url(request):
    project_create_url = reverse("projects:create")
    return {
        "project_create_url":project_create_url,
        "projects_create_url":project_create_url,
    }