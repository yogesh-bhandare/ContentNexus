from django.shortcuts import render
from random import randint

def test_view(request):

    return render(request, "pages/index.html", {})