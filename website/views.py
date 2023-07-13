from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, addRecord
from .models import Students

# Create your views here.
def home(request):

    records = Students.objects.all()

    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")

        user = authenticate(request, username=un, password=pw)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in....')
            return redirect('home')

        else:
            messages.success(request, 'invalied credentials')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out....')
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password1']
            user = authenticate(username=un, password=pw)
            login(request, user)
            messages.success(request, 'Successfully registered')
            return redirect('home')
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})

def std_record(request, pk):
    if request.user.is_authenticated:
        std_rec = Students.objects.get(id=pk)
        return render(request, 'record.html', {'std_rec':std_rec})

    else:
        messages.success(request, "YOu must be logged in")
        return redirect('home')

def del_record(request, pk):
    if request.user.is_authenticated:
        delete = Students.objects.get(id=pk)
        delete.delete()
        messages.success(request, 'record deleted successfully')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in')
        return redirect('home')

def add_record(request):
    form = addRecord(request.POST or None)
    if request.user.is_authenticated:
        if request.method =="POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record added....')
                return redirect('home')

        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, 'You must be logged in')
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        curr_rec = Students.objects.get(id=pk)
        form = addRecord(request.POST or None, instance=curr_rec)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated....')
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, 'You must be logged in')
        return redirect('home')