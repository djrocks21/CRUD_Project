from django.shortcuts import render, redirect
from .forms import StudentRegistration
from registration.models import KeyUser

# Create your views here.


def add_and_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = KeyUser(name=nm, email=em, password=pw)    
            reg.save()
            return redirect("add_and_show")

    else:
        fm = StudentRegistration()

    return render(request, template_name='registration/Add&Show Data.html', context={'form': fm})
















