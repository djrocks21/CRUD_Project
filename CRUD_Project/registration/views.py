from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import StudentRegistration
from registration.models import KeyUser

# Create your views here.


# Below function will add new data & display the data for same --- 

def add_and_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            reg = KeyUser(name=nm, email=em)    
            reg.save()
            fm = StudentRegistration()
            return redirect("add_and_show")

    else:
        fm = StudentRegistration()
    Candidate = KeyUser.objects.all()

    return render(request, template_name='registration/Add&Show Data.html', context={'form': fm, 'cand':Candidate})


# Below function will Update/Edit the data ---


def update_Data(request):
    if request.moethod == "POST":
        Data = KeyUser.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=Data)
        if fm.is_valid():
            fm.save()
        else:
            Data = KeyUser.objects.get(pk=id)
            fm = StudentRegistration(instance=Data)
                
    return render(request, 'registration/UpdateData_Students.html', {'form':fm})

















# Below function will delete the data --- 


def delete_data(request, id):
    if request.method == "POST":
        Data = KeyUser.objects.get(pk=id)
        Data.delete()
        return HttpResponseRedirect('/')

























