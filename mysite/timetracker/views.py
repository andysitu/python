from django.shortcuts import render

from django.utils import timezone

from django.contrib.auth import authenticate, login

def index(request):
    t = timezone.now()
    context = {"month": t.month, "day": t.day, "year": t.year}
    if user is not None:
        context.month = '5353'
    return render(request, 'timetracker/vi)ew.html', context)

def edit_day(request, month, day, year):
    context = {"month": month, "day": day, "year": year}
    return render(request, 'timetracker/edit.html', context)

def view_day(request, month, day, year):
    context = {"month": month, "day": day, "year": year}
    return render(request, 'timetracker/view.html', context)

def test(request):
    # username = request.POST['username']
    # password = request.POST['password']
    user = authenticate(username='a', password='thunder44')
    if user is not None:
        login(request, user)
        t = timezone.now()
        context = {"month": t.month, "day": t.day, "year": t.year}
        return render(request, 'timetracker/view.html', context)