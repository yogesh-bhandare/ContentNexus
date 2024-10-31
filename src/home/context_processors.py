from django.urls import reverse

def site_url(request):
    project_create_url = reverse("projects:create")
    project_deactivate_url = reverse("projects:deactivate")
    project_list_url = reverse("projects:list")
    items_create_url = reverse("items:create")
    items_list_url = reverse("items:list")
    return {
        "project_create_url":project_create_url,
        "projects_create_url":project_create_url,
        "project_deactivate_url":project_deactivate_url,
        "items_create_url":items_create_url,
        "items_list_url":items_list_url,
        "project_list_url":project_list_url,
    }