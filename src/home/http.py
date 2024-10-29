from django.http import HttpResponse
from django_htmx.http import trigger_client_event

def request_refresh_list(request, text=""):
    custom_refresh_event = "refresh-list-view"
    response = HttpResponse("")
    return trigger_client_event(response, custom_refresh_event)