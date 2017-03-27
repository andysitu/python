from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def index(request):
    return HttpResponse("Hellffo")

def detail(request, excel_id):
    context = {"excel_id": excel_id}
    return render(request, 'excel_reader/detail.html', context)

@login_required(login_url='../login/')
def input_file(request):
    print("TEST")
    username = request.POST['username']
    password = request.POST['password']
    print("HI")
    print(username, password)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    return render(request, 'excel_reader/input.html')
