from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import Student, Tutor, Course, Unit, Notes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def StudentRegister(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Student')
            user.groups.add(group)
            
            Student.objects.create(
                user=user
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'Profiles/studentregister.html', context)

def TutorRegister(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Tutor')
            user.groups.add(group)

            Tutor.objects.create(
                user=user
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'Profiles/tutorregister.html', context)


@login_required(login_url='/login/')
def courses(request):
    print("-" * 30)
    print("Hello")
    courses= Course.objects.all()
    return render(request,'Profiles/course-list.html',{'courses':courses})

@login_required(login_url='/login/')
def units(request,un_id):
    unit = Unit.objects.filter(course_id=un_id)
    return render(request,'Profiles/units.html',{"unit": unit})

@login_required(login_url='/login/')
# @allowed_users(allowed_roles=['comrades'])
def notes(request,not_id):
    notes = Notes.objects.filter(unit_id=not_id)
    return render(request,'Profiles/notes.html',{"notes": notes})