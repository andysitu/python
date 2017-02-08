from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")

@login_required(login_url="../login/")
def test_page(request):
    return render(request, "test.html")