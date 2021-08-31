from django.shortcuts import render, redirect
from app1.models import UserModel, Appointment
import time
from datetime import datetime as dt


def index(request):
    return render(request, 'login.html')


def checkLogin(request):
    if request.POST['email'] and request.POST['password']:
        email = request.POST.get('email')
        password = request.POST.get('password')
        if UserModel.objects.filter(email=email) and UserModel.objects.filter(password=password):
            return render(request, 'appointment.html')
        else:
            message = {'message':'Please give valid credentials'}
            return render(request, 'login.html', context=message)


def signUp(request):
    return render(request, 'signup.html')


def saveUser(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    um = UserModel(username=username, email=email, password=password)
    um.save()
    message = {"message": 'Record saved successfully'}
    return render(request, 'login.html', context=message)


def chooseDate(request):
    if request.method == 'GET':
        a = request.GET.get('date')
        mod = Appointment(appointment_date=a)
        b = dt.strptime('09', "%H").time()
        c = dt.strptime(a, "%Y-%m-%dT%H:%M").time()
        d = dt.strptime('17', "%H").time()

        if c >= b and c <= d:
            mod.save()
            return render(request, 'Home.html')
        else:
            return render(request, 'Error.html')
    else:
        message = {"message": 'Invalid date: Appointment time is between 9 AM to 5 PM'}
        return render(request, 'login.html', context=message)
