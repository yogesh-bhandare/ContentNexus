from django.shortcuts import render
from items.models import Item
from projects.decorators import project_required

# Create your views here.
@project_required
def dashboard_view(request):
    # return render(request, "dashboard/home.html", {})
    return render(request, "pages/dashboard.html", {})

def home_page_view(request):
    if not request.user.is_authenticated:
        return render(request, "pages/home.html", {})
    return dashboard_view(request)


