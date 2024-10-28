from django.shortcuts import render
from random import randint

def test_view(request):
    randomVal = randint(1,8)
    context = {
        "obj": randomVal
    }
    return render(request, "test_temp.html", context)