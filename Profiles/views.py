from django.shortcuts import render, redirect
from .forms import CreateUserForm, UserUpdateForm, StudentUpdateForm
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import Student,Tutor
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,TutorRedirect,allowed_users

# Create your views here.
@unauthenticated_user
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

@unauthenticated_user
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

def logoutUser(request):
	logout(request)
	return redirect('/')


@login_required(login_url='login')
@TutorRedirect
def StudentProfile(request):
    return render(request,"Profiles/student/studentprofile.html")

def StudentUpdate(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        sp_form = StudentUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.student)
        if u_form.is_valid() and sp_form.is_valid():
            u_form.save()
            sp_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('studentProfile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        sp_form = StudentUpdateForm(instance=request.user.student)

    context = {
        'u_form': u_form,
        'sp_form': sp_form
    }
    return render(request,'Profiles/student/studentupdate.html', context)


@login_required(login_url='login')
def TutoProfile(request):
    return render(request,"Profiles/Tutor/tutorprofile.html")